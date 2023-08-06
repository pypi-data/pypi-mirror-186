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
import itertools as ittl
from operator import attrgetter as GetAttribute
from operator import itemgetter as ItemAt
from typing import (
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import json_any.json_any as jsnr
from cell_tracking_BC.OLD.standard.uid import Identity
from cell_tracking_BC.OLD.type.cell import cell_t
from cell_tracking_BC.OLD.type.track.all import any_track_h, structured_track_h
from cell_tracking_BC.OLD.type.track.forking import forking_track_t
from cell_tracking_BC.OLD.type.track.single import single_track_t
from cell_tracking_BC.OLD.type.track.unstructured import unstructured_track_t
from cell_tracking_BC.OLD.type.track.structured import (
    cells_w_optional_time_points_h,
    per_single_track_cell_h,
    per_single_track_cells_h,
)
from cell_tracking_BC.OLD.type.tracks.unstructured import unstructured_tracks_t


TrackIssues_h = Callable[
    [structured_track_h, dict], Optional[Union[str, Sequence[str]]]
]


@dtcl.dataclass(repr=False, eq=False)
class tracks_t(List[structured_track_h]):

    invalids: List[Tuple[any_track_h, Sequence[str]]] = dtcl.field(
        init=False, default_factory=list
    )
    fully_pruned: List[structured_track_h] = dtcl.field(
        init=False, default_factory=list
    )

    @classmethod
    def NewFromUnstructuredTracks(cls, tracks: unstructured_tracks_t, /) -> tracks_t:
        """"""
        instance = cls()

        next_single_track_label = 1
        for unstructured in tracks.track_iterator:
            issues = unstructured.Issues()
            if issues is None:
                (
                    forking_track,
                    next_single_track_label,
                ) = forking_track_t.NewFromUnstructuredTrack(
                    unstructured, next_single_track_label
                )

                if forking_track.n_leaves > 1:
                    instance.append(forking_track)
                else:
                    single_track = forking_track.AsSingleTrack()
                    instance.append(single_track)
            else:
                # unstructured.graph["issues"] = issues  # Old, per-track issue storage
                instance.invalids.append((unstructured, issues))

        return instance

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> tracks_t:
        """"""
        return jsnr.ObjectFromJsonString(
            jsoned,
            builders={
                cls.__name__: cls.NewFromJsonDescription,
                "unstructured_track_t": unstructured_track_t.NewFromJsonString,
                "single_track_t": single_track_t.NewFromJsonString,
                "forking_track_t": forking_track_t.NewFromJsonString,
            },
        )

    @classmethod
    def NewFromJsonDescription(
        cls,
        description,
        /,
    ) -> tracks_t:
        """"""
        tracks, attributes = description

        instance = cls.__new__(cls)  # Do not use cls(tracks)
        instance.extend(tracks)
        for key, value in attributes.items():
            setattr(instance, key, value)

        return instance

    @property
    def labels(self) -> Sequence[int]:
        """"""
        output = []

        for track in self:
            output.extend(track.labels)

        return sorted(output)

    def RootCells(
        self, /, *, with_time_point: bool = False
    ) -> cells_w_optional_time_points_h:
        """"""
        if with_time_point:
            what = GetAttribute("root", "root_time_point")
            # output = map(GetAttribute("root", "root_time_point"), self)
            # output = ((_tck.root, _tck.root_time_point) for _tck in self)
        else:
            what = GetAttribute("root")
            # output = map(GetAttribute("root"), self)
            # output = (_tck.root for _tck in self)

        return tuple(map(what, self))

    def MarkDividingCells(
        self,
        before_deaths: bool,
        /,
        *,
        division_responses: Dict[int, Optional[Sequence[float]]] = None,
        lower_bound: float = None,
        CombinedResponse: Callable[[Iterable], float] = max,
    ) -> None:
        """"""
        for track in self:
            if isinstance(track, forking_track_t):
                track.MarkDividingCells(
                    before_deaths,
                    division_responses=division_responses,
                    lower_bound=lower_bound,
                    CombinedResponse=CombinedResponse,
                )

    @property
    def n_dividing_cells(self) -> int:
        """"""
        return sum(_tck.n_dividing_cells for _tck in self)

    def DividingCells(
        self,
        /,
        *,
        with_time_point: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cells_h]:
        """"""
        if per_single_track:
            output = {}
            AddDividing = output.update
        else:
            output = []
            AddDividing = output.extend

        for track in self:
            if isinstance(track, forking_track_t):
                dividing = track.DividingCells(
                    with_time_point=with_time_point, per_single_track=per_single_track
                )
                AddDividing(dividing)

        if with_time_point and not per_single_track:
            output.sort(key=ItemAt(1))

        return output

    def DivisionTimePoints(self) -> Dict[int, Optional[Sequence[int]]]:
        """"""
        output = {}

        for track in self:
            if isinstance(track, forking_track_t):
                time_points = track.DivisionTimePoints()
                output.update(time_points)
            else:
                output[track.label] = None

        return output

    def MarkDeadCells(
        self,
        death_responses: Dict[int, Optional[Sequence[float]]],
        lower_bound: float,
        after_divisions: bool,
        /,
        *,
        CombinedResponse: Callable[[Iterable], float] = max,
    ) -> None:
        """
        A death is set if the highest response at a cell among the adjacent single tracks is above the threshold.
        """
        t_idx = 0
        while t_idx < self.__len__():
            track = self[t_idx]
            track.MarkDeadCells(
                death_responses,
                lower_bound,
                after_divisions,
                CombinedResponse=CombinedResponse,
                called_from_educated_code=True,
            )
            if track.IsFullyPruned():
                self.fully_pruned.append(track)
                del self[t_idx]
            else:
                t_idx += 1

    def DeadCells(
        self,
        sequence_length: int,
        /,
        *,
        with_time_point: bool = False,
        with_living_leaves: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cell_h]:
        """"""
        if per_single_track:
            output = {}
            AddDead = output.update
        else:
            output = []
            AddDead = output.extend

        for track in self:
            dead = track.DeadCells(
                sequence_length,
                with_time_point=with_time_point,
                with_living_leaves=with_living_leaves,
                per_single_track=per_single_track,
            )
            AddDead(dead)

        return output

    def DeathTimePoints(
        self,
        sequence_length: int,
        /,
        *,
        with_living_leaves: bool = False,
    ) -> Dict[int, Optional[int]]:
        """"""
        output = {}

        for track in self:
            time_points = track.DeathTimePoints(
                sequence_length,
                with_living_leaves=with_living_leaves,
            )
            output.update(time_points)

        return output

    def LeafCells(
        self, /, *, with_time_point: bool = False
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cells_h]:
        """"""
        leaves = []
        time_points = []
        for track in self:
            leaves.extend(track.leaves)
            time_points.extend(track.leaves_time_points)

        if with_time_point:
            return tuple(zip(leaves, time_points))

        return tuple(leaves)

    def TrackWithRoot(
        self, root: cell_t, /, *, tolerant_mode: bool = False
    ) -> Optional[structured_track_h]:
        """"""
        for track in self:
            if root is track.root:
                return track

        if tolerant_mode:
            return None

        raise ValueError(f"{root}: Not a root cell")

    def TrackWithCell(
        self, cell: cell_t, /, *, tolerant_mode: bool = False
    ) -> Optional[structured_track_h]:
        """"""
        for track in self:
            if cell in track:
                return track

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Cell not in any track")

    def TrackWithLeaf(
        self, leaf: cell_t, /, *, tolerant_mode: bool = False,
        geometric_mode: bool = False,
    ) -> Optional[single_track_t]:
        """
        Implicitly, it is SingleTrackWithLeaf
        """
        for track in self:
            if geometric_mode:
                leaves = track.geometric_leaves
            else:
                leaves = track.leaves
            if leaf in leaves:
                return track.TrackWithLeaf(leaf, check=False, geometric_mode=geometric_mode)
            # for cell in track.leaves:
            #     if leaf is cell:
            #         return track.TrackWithLeaf(cell, check=False)

        if tolerant_mode:
            return None

        raise ValueError(f"{leaf}: Not a leaf cell")

    def TrackWithLabel(
        self, label: int, /, *, tolerant_mode: bool = False, geometric_mode: bool = False,
    ) -> Optional[single_track_t]:
        """
        Implicitly, it is SingleTrackWithLabel
        """
        for track in self:
            if isinstance(track, single_track_t):
                if track.label == label:
                    if geometric_mode:
                        return track
                    else:
                        return track.unpruned_piece
            else:
                if geometric_mode:
                    iterator = track.geometric_single_tracks_iterator
                else:
                    iterator = track.single_tracks_iterator
                for single_track in iterator:
                    if single_track.label == label:
                        return single_track

        if tolerant_mode:
            return None

        raise ValueError(f"{label}: Not a valid track label")

    @property
    def single_tracks_iterator(self) -> Iterator[single_track_t]:
        """"""
        for track in self:
            # Do not just yield track if it is a single track since it would not account for pruning
            for single_track in track.single_tracks_iterator:
                yield single_track

    @property
    def geometric_single_tracks_iterator(
        self,
    ) -> Iterator[single_track_t]:
        """"""
        for track in self:
            for single_track in track.geometric_single_tracks_iterator:
                yield single_track

    def TrackLabelsContainingCell(
        self, cell: cell_t, /, *, tolerant_mode: bool = False
    ) -> Optional[Sequence[int]]:
        """"""
        for track in self:
            if cell in track:
                return track.TrackLabelsContainingCell(
                    cell, check=False, tolerant_mode=tolerant_mode
                )

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Not a tracked cell")

    # def TrackLabelWithLeaf(
    #     self, leaf: cell_t, /, *, tolerant_mode: bool = False
    # ) -> Optional[int]:
    #     """
    #     TrackLabelWithLeaf: Implicitly, it is SingleTrackLabelWithLeaf
    #     """
    #     track = self.TrackWithLeaf(leaf, tolerant_mode=True)
    #     if track is not None:
    #         return track.label
    #
    #     if tolerant_mode:
    #         return None
    #
    #     raise ValueError(f"{leaf}: Not a leaf cell")

    def FilterOut(
        self,
        TrackIssues: TrackIssues_h,
        /,
        **kwargs,
    ) -> None:
        """
        Parameters
        ----------
        TrackIssues: Arguments are: track and (optional) keyword arguments; Returned value can be None, an str, or a
            sequence of str.
        kwargs: Passed to TrackIsInvalid as keyword arguments
        """
        t_idx = 0
        while t_idx < self.__len__():
            track = self[t_idx]
            issues = TrackIssues(track, **kwargs)
            if issues is None:
                t_idx += 1
            else:
                self.invalids.append((track, issues))
                del self[t_idx]

    def AsJsonString(self) -> str:
        """"""
        # Do not use dtcl.asdict(self) since it recurses into dataclass instances which, if they extend a "container"
        # class like list or dict, will lose the contents.
        attributes = {_fld.name: getattr(self, _fld.name) for _fld in dtcl.fields(self)}

        # list(self): To hide this method, which would otherwise be infinitely recursively called
        return jsnr.JsonStringOf((list(self), attributes), true_type=self)

    def Print(self) -> None:
        """"""
        for track in self:
            print(track)

    def __repr__(self) -> str:
        """"""
        return Identity(self)

    def __str__(self) -> str:
        """"""
        return f"{self.__repr__()}:\n    {self.__len__()=}\n    {self.invalids=}\n    {self.fully_pruned=}"

    def __eq__(self, other) -> bool:
        """"""
        if hasattr(other, "AsJsonString"):
            return self.AsJsonString() == other.AsJsonString()

        return False


def UniqueCellsFromPerSingleTrackOnes(
    per_single_track: per_single_track_cells_h,
    /,
    *,
    should_remove_time_point: bool = False,
) -> cells_w_optional_time_points_h:
    """
    Per single track dividing cells => Single-track-label-indexed dictionary with cells repeated among the values.
    This function removes the redundancy among the dividing cells dictionary values.
    """
    cells = ittl.chain.from_iterable(per_single_track.values())
    if should_remove_time_point:
        cells = map(ItemAt(0), cells)

    return tuple(set(cells))
