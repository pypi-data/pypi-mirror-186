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

from pathlib import Path as path_t
from typing import Callable, Optional, Tuple, Union

import imageio as mgio
import mrc as mrci
import numpy as nmpy
import tifffile as tiff

import cell_tracking_BC.OLD.in_out.file.frame as frio
from cell_tracking_BC.OLD.in_out.graphics.dbe.matplotlib.context import DRAWING_CONTEXT
from cell_tracking_BC.OLD.in_out.graphics.generic.d_2 import (
    AsAnnotatedVolume,
    FigureAxesAndDrawer,
)
from cell_tracking_BC.OLD.in_out.graphics.type.context import context_t
from cell_tracking_BC.OLD.type.sequence import BoundingBoxSlices, sequence_t


array_t = nmpy.ndarray


# TODO: check the output format of the different functions. In particular, do they all output the time dimension as the
#       last one?
# TODO: Probably add (generic) parameters to specify eventual required hints for reading function such as number of
#       channels...


def SequenceByITK(path: path_t, /) -> array_t:
    """
    Shape: time*channel x row x col
    """
    return frio.FrameByITK(path)


def SequenceByIMAGEIO(path: path_t, /) -> array_t:
    """"""
    return mgio.volread(path)


def SequenceFromPath(
    path: path_t,
    /,
    *,
    SequenceLoading: Callable[[path_t], array_t] = SequenceByIMAGEIO,
) -> array_t:
    """"""
    # TODO: make this function work in "every" cases (add a parameter about expected dimension arrangements), or
    #       remove the sequence loading functionality from cell-tracking-bc, leaving this task to the end user.
    if not (path.exists() and path.is_file()):
        raise ValueError(f"{path}: Not a path to an existing file")

    if (img_format := path.suffix[1:].lower()) in ("tif", "tiff"):
        output = tiff.imread(str(path))
    elif img_format in ("dv", "mrc"):
        # numpy.array: Because the returned value seems to be a read-only memory map
        output = nmpy.array(mrci.imread(str(path)))
        if output.ndim == 5:
            # Probably: time x channel x Z x Y x X while sequences are time x channel x (Z=1 x) Y x X, so one gets:
            # time x channel=1 x Z=actual channels x Y x X
            output = output[:, 0, :, :]
    else:
        output = SequenceLoading(path)

    return output


def SaveAnnotatedSequence(
    sequence: sequence_t,
    path: Union[str, path_t],
    /,
    *,
    channel: str = None,
    with_segmentation: bool = True,
    with_cell_labels: bool = True,
    with_track_labels: bool = True,
    as_sequence: bool = True,
    should_draw_frame: bool = True,
    dbe: context_t = DRAWING_CONTEXT,
) -> None:
    """
    channel: None=segmentation channel
    """
    folder, basename, extension, channel = _PathsForAnnotatedSequence(
        sequence, path, channel
    )

    figure, axes, drawer = FigureAxesAndDrawer(
        dbe.figure_2d_t,
        dbe.s_drawer_2d_t,
        sequence,
        channel,
        with_segmentation,
        with_cell_labels,
        with_track_labels,
        dbe,
        False,
    )

    volume = None  # Cannot be initialized since content (not frame) shape is unknown
    for time_point in range(sequence.length):
        drawer.SelectVersionAndTimePoint(
            time_point=time_point,
            should_draw_frame=should_draw_frame,
            should_update_figure=False,
        )
        figure.Update(gently=False)  # draw_idle is not appropriate here
        if as_sequence:
            content = figure.Content()
            if volume is None:
                volume = nmpy.empty((*content.shape, sequence.length), dtype=nmpy.uint8)
            volume[..., time_point] = content
        else:
            figure.Save(folder / f"{basename}_{time_point}{extension}")

    figure.Close()  # To prevent remaining caught in event loop

    if as_sequence:
        _SaveSequence(volume, path)


def SaveAnnotatedSequenceMPL(
    sequence: sequence_t,
    path: Union[str, path_t],
    /,
    *,
    channel: str = None,
    with_segmentation: bool = True,
    with_cell_labels: bool = True,
    with_track_labels: bool = True,
    should_draw_frame: bool = True,
    as_sequence: bool = True,
) -> None:
    """
    channel: None=segmentation channel
    """
    folder, basename, extension, channel = _PathsForAnnotatedSequence(
        sequence, path, channel
    )

    if as_sequence:
        SaveFrame = None
    else:
        SaveFrame = lambda _cnt, _tmp: mgio.imwrite(
            folder / f"{basename}_{_tmp}{extension}", _cnt
        )
    volume = AsAnnotatedVolume(
        sequence,
        channel,
        with_segmentation,
        with_cell_labels,
        with_track_labels,
        should_draw_frame=should_draw_frame,
        SaveFrame=SaveFrame,
    )

    if volume is not None:
        _SaveSequence(volume, path)


def _PathsForAnnotatedSequence(
    sequence: sequence_t, path: Union[str, path_t], channel: Optional[str], /
) -> Tuple[path_t, str, str, str]:
    """"""
    if isinstance(path, str):
        path = path_t(path)
    if channel is None:
        channel = sequence.cell_channel

    folder = path.parent
    basename = path.stem
    extension = path.suffix

    return folder, basename, extension, channel


def _SaveSequence(sequence: array_t, path: path_t, /) -> None:
    """"""
    row_slice, col_slice = BoundingBoxSlices(sequence)
    sequence = sequence[row_slice, col_slice, :, :]
    sequence = nmpy.moveaxis(sequence, (0, 1, 2, 3), (2, 3, 1, 0))
    sequence = sequence[:, nmpy.newaxis, :, :, :]

    tiff.imwrite(
        str(path),
        sequence,
        photometric="rgb",
        compression="deflate",
        planarconfig="separate",
        metadata={"axes": "XYZCT"},
    )
