# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from __future__ import annotations

import dataclasses as dtcl
import functools as fctl
from itertools import starmap, zip_longest
import json
from multiprocessing import Pool as pool_t
from operator import attrgetter as GetAttribute
from pathlib import Path as path_t
from typing import Any, Callable, Dict, Iterator, Optional, Sequence, Tuple, Union

# import blosc as blsc
import numpy as nmpy
import scipy.ndimage as imge
from skimage.transform import resize as Resize

import json_any.json_any as jsnr
import cell_tracking_BC.OLD.in_out.text.progress as prgs
import cell_tracking_BC.OLD.standard.issue as isse
from cell_tracking_BC.OLD.in_out.text.logger import LOGGER
from cell_tracking_BC.OLD.standard.number import MAX_INT
from cell_tracking_BC.OLD.standard.uid import Identity
from cell_tracking_BC.OLD.type.cell import cell_t
from cell_tracking_BC.OLD.type.cytoplasm import cytoplasm_t
from cell_tracking_BC.OLD.type.frame import frame_t, transform_h
from cell_tracking_BC.OLD.type.nucleus import nucleus_t
from cell_tracking_BC.OLD.type.segmentation import compartment_t, segmentation_t
from cell_tracking_BC.OLD.type.segmentations import segmentations_t
from cell_tracking_BC.OLD.type.track.forking import forking_track_t
from cell_tracking_BC.OLD.type.track.single import single_track_t
from cell_tracking_BC.OLD.type.track.structured import (
    feature_filtering_h,
    per_single_track_feature_h,
)
from cell_tracking_BC.OLD.type.track.unstructured import unstructured_track_t
from cell_tracking_BC.OLD.type.tracks.structured import tracks_t


array_t = nmpy.ndarray
#
all_versions_h = Dict[
    str, Tuple[Tuple[int, int], Union[Sequence[array_t], Sequence[frame_t]]]
]
channel_computation_h = Callable[[Dict[str, array_t], Dict[str, Any]], array_t]
morphological_feature_computation_h = Callable[
    [cell_t, Dict[str, Any]], Union[Any, Sequence[Any]]
]
radiometric_feature_computation_h = Callable[
    [cell_t, Union[array_t, Sequence[array_t]], Dict[str, Any]],
    Union[Any, Sequence[Any]],
]


@dtcl.dataclass(repr=False, eq=False)
class sequence_t(dict):
    """
    dict=Dict[str, Sequence[Union[bytes, array_t, frame_t]]]
    """

    path: Optional[path_t] = None
    shape: Tuple[int, int] = None
    original_length: int = None
    first_frame: int = None
    length: int = None
    base_channels: Sequence[str] = None
    # frames_of_channel: Dict[str, Sequence[Union[bytes, array_t, frame_t]]] = None
    # Name of channel whose frames store the segmented cells
    cell_channel: str = dtcl.field(init=False, default=None)
    segmentations: segmentations_t = dtcl.field(init=False, default=None)
    tracks: tracks_t = dtcl.field(init=False, default=None)

    @classmethod
    def NewFromFrames(
        cls,
        frames: array_t,
        in_channel_names: Sequence[Optional[str]],
        path: path_t,
        /,
        *,
        first_frame: int = 0,
        last_frame: int = MAX_INT,
        expected_shape: Sequence[int] = None,
    ) -> sequence_t:
        """
        in_channel_names: names equal to None or "___" or "---" indicate channels that should be discarded
        """
        # TODO: make this function accept various input shapes thanks to an additional arrangement parameter of the
        #     form THRC, T=time, H=channel, RC= row column. This requires that SequenceFromPath deals with TH combined
        #     dimension.
        if (n_dims := frames.ndim) not in (3, 4):
            raise ValueError(
                f"{n_dims}: Invalid number of dimensions of sequence with shape {frames.shape}. "
                f"Expected=3 or 4=(TIME POINTS*CHANNELS)xROWSxCOLUMNS or "
                f"TIME POINTSxCHANNELSxROWSxCOLUMNS."
            )
        n_in_channels = in_channel_names.__len__()

        if n_dims == 3:
            frames = frames[
                (first_frame * n_in_channels) : ((last_frame + 1) * n_in_channels), ...
            ]
        else:
            frames = frames[first_frame : (last_frame + 1), ...]
        first_frame = 0
        last_frame = MAX_INT

        if expected_shape is not None:
            if n_dims == 3:
                order_in = (0, 1, 2)
                order_out = (2, 0, 1)
                fixed_size = frames.shape[:1]
                to_be_resized = frames.shape[1:]
            else:
                order_in = (0, 1, 2, 3)
                order_out = (2, 3, 0, 1)
                fixed_size = frames.shape[:2]
                to_be_resized = frames.shape[2:]
            if to_be_resized != expected_shape:
                LOGGER.warn(
                    f"Resizing sequence from actual size {to_be_resized} (full shape={frames.shape}) "
                    f"to expected size {expected_shape}"
                )
                frames = nmpy.moveaxis(frames, order_in, order_out)
                frames = Resize(
                    frames, (*expected_shape, *fixed_size), preserve_range=True
                )
                frames = nmpy.moveaxis(frames, order_out, order_in)
                LOGGER.info(f"Resizing done. New sequence shape={frames.shape}")

        frames_of_channel = {}
        for name in in_channel_names:
            if (name is not None) and (name != "___") and (name != "---"):
                frames_of_channel[name] = []
        base_channel_names = tuple(frames_of_channel.keys())

        if n_dims == 3:
            c_idx = n_in_channels - 1
            time_point = -1
            for raw_frame in frames:
                c_idx += 1
                if c_idx == n_in_channels:
                    c_idx = 0
                    time_point += 1

                if time_point < first_frame:
                    continue
                elif time_point > last_frame:
                    break

                name = in_channel_names[c_idx]
                if name in base_channel_names:
                    frame = frame_t(raw_frame)
                    frames_of_channel[name].append(frame)
        else:
            for time_point, raw_frame in enumerate(frames):
                if time_point < first_frame:
                    continue
                elif time_point > last_frame:
                    break

                for c_idx, channel in enumerate(raw_frame):
                    name = in_channel_names[c_idx]
                    if name in base_channel_names:
                        frame = frame_t(channel)
                        frames_of_channel[name].append(frame)

        frames_of_base_channel = frames_of_channel[base_channel_names[0]]
        shape = frames_of_base_channel[0].shape
        length = frames_of_base_channel.__len__()
        instance = cls(
            path=path,
            shape=shape,
            original_length=frames.__len__(),
            first_frame=first_frame,
            length=length,
            base_channels=base_channel_names,
            # frames_of_channel=frames_of_channel,
        )
        instance.update(frames_of_channel)

        return instance

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> sequence_t:
        """"""
        return jsnr.ObjectFromJsonString(
            jsoned,
            builders={
                cls.__name__: cls.NewFromJsonDescription,
                "segmentations_t": segmentations_t.NewFromJsonString,
                "tracks_t": tracks_t.NewFromJsonString,
                "frame_t": frame_t.NewFromJsonString,
            },
        )

    @classmethod
    def NewFromJsonDescription(
        cls,
        description: Tuple[
            Dict[str, Sequence[Union[bytes, array_t, frame_t]]], Dict[str, Any]
        ],
        /,
    ) -> sequence_t:
        """"""
        frames, attributes = description

        instance = cls(
            path=attributes["path"],
            shape=attributes["shape"],
            original_length=attributes["original_length"],
            first_frame=attributes["first_frame"],
            length=attributes["length"],
            base_channels=attributes["base_channels"],
        )
        instance.update(frames)
        instance.cell_channel = attributes["cell_channel"]
        instance.segmentations = attributes["segmentations"]
        instance.tracks = attributes["tracks"]

        return instance

    def __len__(self) -> int:
        """"""
        return self.length

    @property
    def channels(self) -> Sequence[str]:
        """
        Names of channels read from file (base channels) and computed channels
        """
        # return tuple(self.frames_of_channel.keys())
        return tuple(self.keys())

    def Frames(
        self,
        /,
        *,
        channel: Union[str, Sequence[str]] = None,
    ) -> Union[
        Sequence[Union[array_t, frame_t]],
        Iterator[Sequence[Union[array_t, frame_t]]],
    ]:
        """
        channel: None=all (!) base channels; Otherwise, only (a) base channel name(s) can be passed
        as_iterator: Always considered True if channel is None or a sequence of channel names
        """
        if isinstance(channel, str):
            # return _AsArraySequence(self.frames_of_channel[channel])
            return _AsArraySequence(self[channel])
        else:
            return self._FramesForMultipleChannels(channel)

    def _FramesForMultipleChannels(
        self, channels: Optional[Sequence[str]], /
    ) -> Iterator[Sequence[Union[array_t, frame_t]]]:
        """
        /!\ If "channels" contains both base and non-base channels, then the returned tuples will contain both array_t
        and frame_t elements (but frame_t is a subclass of array_t, so...).
        """
        if channels is None:
            channels = self.base_channels

        for f_idx in range(self.length):
            # frames = tuple(self.frames_of_channel[_chl][f_idx] for _chl in channels)
            frames = tuple(self[_chl][f_idx] for _chl in channels)
            output = []
            for frame in frames:
                # if isinstance(frame, bytes):
                #     frame = blsc.unpack_array(frame)
                output.append(frame)

            yield output

    def ChannelExtrema(self, channel: str, /) -> Tuple[float, float]:
        """"""
        min_intensity = nmpy.Inf
        max_intensity = -nmpy.Inf

        # for frame in _AsArraySequence(self.frames_of_channel[channel]):
        for frame in _AsArraySequence(self[channel]):
            min_intensity = min(min_intensity, nmpy.amin(frame))
            max_intensity = max(max_intensity, nmpy.amax(frame))

        # Apparently, the intensities might not be Numpy object in certain situations (Numpy version?). Although
        # currently unexplained, an easy workaround is to return the intensities as is.
        try:
            output = min_intensity.item(), max_intensity.item()
        except AttributeError:
            output = min_intensity, max_intensity

        return output

    @property
    def has_cells(self) -> bool:
        """"""
        return self.cell_channel is not None

    def NCells(
        self, /, *, in_frame: Union[int, Sequence[int]] = None
    ) -> Union[int, Sequence[int]]:
        """
        in_frame: None=>total over the sequence
        """
        if in_frame is None:
            return sum(_cll.__len__() for _cll in self.cells_iterator)

        just_one = isinstance(in_frame, int)
        if self.has_cells:
            if just_one:
                in_frame = (in_frame,)

            output = in_frame.__len__() * [0]

            for f_idx, cells in enumerate(self.cells_iterator):
                if f_idx in in_frame:
                    output[in_frame.index(f_idx)] = cells.__len__()

            if just_one:
                output = output[0]
        elif just_one:
            output = 0
        else:
            output = in_frame.__len__() * (0,)

        return output

    @property
    def cell_frames(self) -> Sequence[frame_t]:
        """
        /!\ It is assumed that self.frames_of_channel[self.cell_channel] are frame_t's, not bytes
        """
        # return self.frames_of_channel[self.cell_channel]
        return self[self.cell_channel]

    @property
    def cells_iterator(self) -> Iterator[Sequence[cell_t]]:
        """"""
        for frame in self.cell_frames:
            yield frame.cells

    @property
    def cytoplasms_iterator(self) -> Iterator[Sequence[Optional[cytoplasm_t]]]:
        """"""
        for frame in self.cell_frames:
            yield tuple(map(GetAttribute("cytoplasm"), frame.cells))
            # output = []
            # for cell in frame.cells:
            #     output.append(cell.cytoplasm)
            # yield output

    @property
    def nuclei_iterator(self) -> Iterator[Sequence[Sequence[nucleus_t]]]:
        """"""
        for frame in self.cell_frames:
            yield tuple(map(GetAttribute("nuclei"), frame.cells))
            # output = []
            # for cell in frame.cells:
            #     output.append(cell.nuclei)
            # yield output

    def ApplyTransform(
        self,
        Transform: transform_h,
        /,
        *,
        channel: Union[str, Sequence[str]] = None,
        **kwargs,
    ) -> None:
        """
        /!\ It is assumed that self.frames_of_channel[channel] are frame_t's, not bytes
        channel: None=all (!)
        """
        if channel is None:
            channels = self.base_channels
        elif isinstance(channel, str):
            channels = (channel,)
        else:
            channels = channel

        for channel in channels:
            # targets = self.frames_of_channel[channel]
            targets = self[channel]
            if not isinstance(targets[0], frame_t):
                raise ValueError(
                    f"{type(targets[0]).__name__}: Invalid type of channel {channel} "
                    f"for {sequence_t.ApplyTransform.__name__}. Expected={frame_t.__name__}"
                )
            references_sets = self.Frames(channel=self.channels)
            for target, references in zip(targets, references_sets):
                refs_as_dict = dict(zip(self.channels, references))
                # refs_as_dict = {
                #     _nme: _frm for _nme, _frm in zip(self.channels, references)
                # }
                target.ApplyTransform(Transform, channels=refs_as_dict, **kwargs)

    def AddChannel(
        self, name: str, ChannelComputation: channel_computation_h, /, **kwargs
    ) -> None:
        """"""
        # if name in self.frames_of_channel:
        if name in self:
            raise ValueError(f"{name}: Existing channel cannot be overridden")

        computed = []
        for frames in self.Frames(channel=self.channels):
            frames_as_dict = dict(zip(self.channels, frames))
            # frames_as_dict = {_nme: _frm for _nme, _frm in zip(self.channels, frames)}
            frame = ChannelComputation(frames_as_dict, **kwargs)
            computed.append(frame)  # blsc.pack_array(frame))

        # self.frames_of_channel[name] = computed
        self[name] = computed

    def AddCellsFromSegmentations(
        self,
        channel: str,
        segmentations: segmentations_t,
    ) -> None:
        """
        Segmentation are supposed to be binary (as opposed to already labeled)
        """
        self.cell_channel = channel
        self.segmentations = segmentations

        for frame, segmentation in zip(self.cell_frames, segmentations):
            frame.AddCellsFromSegmentation(segmentation)

    def AddCellFeature(
        self,
        name: Union[str, Sequence[str]],
        Feature: Union[
            morphological_feature_computation_h, radiometric_feature_computation_h
        ],
        /,
        channel: Union[str, Sequence[str]] = None,
        should_run_in_parallel: bool = True,
        should_run_silently: bool = False,
        **kwargs,
    ) -> None:
        """
        name: If an str, then the value returned by Feature will be considered as a whole, whether it is actually a
        single value or a value container. If a sequence of str's, then the object returned by Feature will be iterated
        over, each element being matched with the corresponding name in "name".
        channel: if None, then morphological feature, else radiometric feature.

        /!\ There is no already-existing check
        """
        if isinstance(name, str):
            description = f'Feature "{name}"'
        elif name.__len__() > 2:
            description = f'Feature "{name[0]}, ..., {name[-1]}"'
        else:
            description = f'Feature "{name[0]}, {name[1]}"'
        ParallelFeature = fctl.partial(Feature, **kwargs)

        with prgs.ProgressDesign(should_be_silent=should_run_silently) as progress:
            if channel is None:
                iterator = self.cells_iterator
            else:
                # iterator = zip(self.cells_iterator, _AsArraySequence(self.frames_of_channel[channel]))
                iterator = zip(self.cells_iterator, _AsArraySequence(self[channel]))
            progress_context = prgs.progress_context_t(
                progress,
                iterator,
                total=self.length,
                description=description,
            )

            if should_run_in_parallel:
                pool = pool_t()
                MapFunctionOnList = pool.map
                StarMapFunctionOnList = pool.starmap
            else:
                pool = None
                MapFunctionOnList = map
                StarMapFunctionOnList = starmap

            if channel is None:
                if isinstance(name, str):
                    for cells in progress_context.elements:
                        features = MapFunctionOnList(ParallelFeature, cells)
                        for cell, feature in zip(cells, features):
                            cell.AddFeature(name, feature)
                else:
                    names = name
                    for cells in progress_context.elements:
                        multi_features = MapFunctionOnList(ParallelFeature, cells)
                        for cell, features in zip(cells, multi_features):
                            for name, feature in zip(names, features):
                                cell.AddFeature(name, feature)
            else:
                if isinstance(name, str):
                    for cells, frame in progress_context.elements:
                        features = StarMapFunctionOnList(
                            ParallelFeature,
                            zip_longest(cells, (frame,), fillvalue=frame),
                        )
                        for cell, feature in zip(cells, features):
                            cell.AddFeature(name, feature)
                else:
                    names = name
                    for cells, frame in progress_context.elements:
                        multi_features = StarMapFunctionOnList(
                            ParallelFeature,
                            zip_longest(cells, (frame,), fillvalue=frame),
                        )
                        for cell, features in zip(cells, multi_features):
                            for name, feature in zip(names, features):
                                cell.AddFeature(name, feature)

            if should_run_in_parallel:
                pool.close()
                pool.terminate()

    @property
    def available_cell_features(self) -> Sequence[str]:
        """"""
        one_cell = self.cell_frames[0].cells[0]

        return one_cell.available_features

    def AddTracks(
        self,
        tracks: tracks_t,
        /,
    ) -> None:
        """"""
        self.tracks = tracks

    def AddTrackFeature(
        self,
        name: str,
        cell_feature_name: Union[str, Sequence[str]],
        FeatureComputation: feature_filtering_h,
        /,
        *args,
        geometric_mode: bool = False,
        **kwargs,
    ) -> None:
        """
        /!\ There is no already-existing check
        """
        if isinstance(cell_feature_name, str):
            cell_feature_names = (cell_feature_name,)
        else:
            cell_feature_names = cell_feature_name
        if any(_ftr not in self.available_cell_features for _ftr in cell_feature_names):
            raise ValueError(f"{cell_feature_name}: Invalid cell feature(s)")

        for track in self.tracks:
            track.AddFeature(
                name, cell_feature_names, FeatureComputation, *args, geometric_mode=geometric_mode, **kwargs
            )

    def CellFeature(
        self, feature: str, /, *, geometric_mode: bool = False
    ) -> Dict[int, Tuple[single_track_t, Sequence[Any]]]:
        """"""
        output = {}

        if geometric_mode:
            tracks = self.tracks.geometric_single_tracks_iterator
        else:
            tracks = self.tracks.single_tracks_iterator
        for track in tracks:
            output[track.label] = (
                track,
                track.CellFeature(feature, geometric_mode=geometric_mode),
            )

        return output

    def TrackFeature(self, feature: str, /) -> per_single_track_feature_h:
        """"""
        output = {}

        for track in self.tracks:
            output.update(track.features[feature])

        return output

    def DescriptionOfFrame(self, frame_idx: int, /) -> Dict[str, Any]:
        """"""
        output = {}

        track_labels = []
        for cell in self.cell_frames[frame_idx].cells:
            labels = self.tracks.TrackLabelsContainingCell(cell, tolerant_mode=True)
            if labels is None:
                text = ""  # "i"  # Invalid
            elif labels.__len__() == 0:
                text = "p"  # Pruned
            elif labels.__len__() > 1:
                text = "\n".join(str(_lbl) for _lbl in labels)
            else:
                text = str(labels[0])
            track_labels.append((text, cell.centroid))
        output["track_labels"] = tuple(track_labels)

        return output

    def ClearContents(self):
        """
        To free up some memory when all processing has been done
        """
        for frames in self.Frames():
            for frame in frames:
                frame.ClearContents()

    def PrintValidInvalidTrackSummary(self) -> None:
        """"""
        n_invalids = []
        issues_per_type = {}
        for track_type in (unstructured_track_t, single_track_t, forking_track_t):
            invalids = [
                _rcd for _rcd in self.tracks.invalids if isinstance(_rcd[0], track_type)
            ]
            track_type = track_type.__name__[:-2].replace("_", " ").capitalize()
            if invalids.__len__() == 0:
                number = f"{track_type}: None"
            else:
                number = f"{track_type}: {invalids.__len__()}"

                issues = (
                    f"    Track {_tck.labels_as_str}{isse.ISSUE_SEPARATOR}"
                    f"{isse.FactorizedIssuesAsStr(_iss, max_n_contexts=5)}"
                    for _tck, _iss in invalids
                )
                issues_per_type[track_type] = "\n".join(issues)

            n_invalids.append(number)

        n_invalids = ", ".join(n_invalids)
        issues_per_type = "\n".join(
            f"{_typ}:\n{_iss}" for _typ, _iss in issues_per_type.items()
        )

        print(
            f"Tracks: valid={self.tracks.__len__()}; "
            f"invalid={n_invalids}; "
            f"fully pruned={self.tracks.fully_pruned.__len__()}\n"
            f"{issues_per_type}"
        )

    def AsJsonString(self) -> str:
        """"""
        # Do not use dtcl.asdict(self) since it recurses into dataclass instances which, if they extend a "container"
        # class like list or dict, will lose the contents.
        attributes = {_fld.name: getattr(self, _fld.name) for _fld in dtcl.fields(self)}

        # dict(self): To hide this method, which would otherwise be infinitely recursively called
        return jsnr.JsonStringOf((dict(self), attributes), true_type=self)

    def __repr__(self) -> str:
        """"""
        return Identity(self)

    def __str__(self) -> str:
        """"""
        if self.tracks is None:
            invalid_tracks = None
            fully_pruned_tracks = None
        else:
            invalid_tracks = str(self.tracks.invalids)
            fully_pruned_tracks = str(self.tracks.fully_pruned)

        all_extrema = []
        for channel in self.channels:
            extrema = self.ChannelExtrema(channel)
            all_extrema.append(f"{channel}=[{extrema[0]},{extrema[1]}]")
        all_extrema = "\n    ".join(all_extrema)

        return (
            f"{repr(self)}:\n"
            f"    {self.path=}\n"
            f"    {self.base_channels=}\n"
            f"    {self.channels=}\n"
            f"    {all_extrema}\n"
            f"    {self.shape=}\n"
            f"    {self.original_length=}\n"
            f"    {self.length=}\n"
            f"    {self.tracks=}\n"
            f"    {invalid_tracks=}\n"
            f"    {fully_pruned_tracks=}\n"
        )

    def __eq__(self, other) -> bool:
        """"""
        if hasattr(other, "AsJsonString"):
            return self.AsJsonString() == other.AsJsonString()

        return False

    def __hash__(self) -> int:
        """"""
        return hash((self.path, self.shape, self.first_frame, self.length))


sequence_h = Union[
    Sequence[array_t], Sequence[segmentation_t], segmentations_t, sequence_t
]


def _AsArraySequence(
    frames: Union[Sequence[bytes], Sequence[array_t]], /
) -> Sequence[array_t]:
    """"""
    # if isinstance(frames[0], bytes):
    #     return tuple(map(blsc.unpack_array, frames))

    return frames


def _JsonableFrame(
    frame: Union[bytes, array_t, frame_t], /
) -> Tuple[str, Union[array_t, str]]:
    """"""
    if isinstance(frame, bytes):
        output = ("bytes", frame)  # pcst.BStream2PCA(frame))
    # Test frame_t first (instead of array_t) since a frame_t is also an array_t
    elif isinstance(frame, frame_t):
        output = ("frame_t", frame.AsJsonString())
    else:
        output = ("array_t", frame)

    return output  # jsnr.JsonStringOf(output)


def _FrameFromJsonString(jsoned: Sequence, /) -> Union[bytes, array_t, frame_t]:
    """"""
    if isinstance(jsoned, str):
        jsoned = json.loads(jsoned)
    type_, frame = jsoned
    if type_ not in ("array_t", "bytes", "frame_t"):
        type_ = json.loads(type_)

    if type_ == "bytes":
        return bytes.fromhex(
            json.loads(frame)
        )  # .encode(encoding="raw-unicode-escape")#pcst.PCA2BStream(nmpy.array(json.dumps(frame)))
    if type_ == "array_t":
        return nmpy.array(json.loads(frame))

    return frame_t.NewFromJsonString(frame)


def BoundingBoxSlices(sequence: array_t, /) -> Tuple[slice, slice]:
    """
    sequence: as an XYCT-volume
    """
    min_reduction = nmpy.amin(sequence, axis=-1)
    max_reduction = nmpy.amax(sequence, axis=-1)
    variable = nmpy.any(min_reduction != max_reduction, axis=-1)

    output = imge.find_objects(variable.astype(nmpy.int8))
    if output.__len__() == 0:
        raise ValueError(f"{sequence}: Empty sequence")

    return output[0]


def AllChannelsOfSequence(
    sequence: Union[Sequence[array_t], sequence_t]
) -> Tuple[all_versions_h, str]:
    """"""
    if isinstance(sequence, sequence_t):
        all_channels = {}
        for channel in sequence.channels:
            frames = sequence.Frames(channel=channel)
            min_value = min(nmpy.amin(_frm) for _frm in frames)
            max_value = max(nmpy.amax(_frm) for _frm in frames)
            all_channels[channel] = ((min_value, max_value), frames)
        current_channel = sequence.channels[0]
    else:
        current_channel = "MAIN"
        min_value = min(nmpy.amin(_frm) for _frm in sequence)
        max_value = max(nmpy.amax(_frm) for _frm in sequence)
        all_channels = {current_channel: ((min_value, max_value), sequence)}

    return all_channels, current_channel


def AllSegmentationsOfSequence(sequence: sequence_h) -> Tuple[all_versions_h, str]:
    """"""
    if isinstance(sequence, (segmentations_t, sequence_t)):
        if isinstance(sequence, segmentations_t):
            segmentations = sequence
        else:
            segmentations = sequence.segmentations

        all_versions = {}
        compartments, versions = segmentations.available_versions
        for compartment in compartments:
            for version in versions:
                key = f"{compartment.name}:{version[0]}:{version[1]}"
                frames = segmentations.CompartmentsWithVersion(
                    compartment, index=version[0], name=version[1]
                )
                all_versions[key] = ((0, 1), frames)
        current_version = f"{compartment_t.CELL.name}:{versions[0][0]}:{versions[0][1]}"
    else:
        current_version = "MAIN"
        all_versions = {current_version: ((0, 1), sequence)}

    return all_versions, current_version


def AllStreamsOfSequence(sequence: sequence_t) -> Tuple[all_versions_h, str]:
    """"""
    all_streams, current_stream = AllChannelsOfSequence(sequence)
    all_versions, _ = AllSegmentationsOfSequence(sequence)

    all_streams.update(all_versions)

    return all_streams, current_stream
