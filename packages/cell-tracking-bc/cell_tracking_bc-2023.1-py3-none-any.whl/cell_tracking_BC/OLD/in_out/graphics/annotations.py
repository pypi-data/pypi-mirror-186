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

import time
from pathlib import Path as path_t
from typing import Union

import matplotlib.pyplot as pypl
import numpy as nmpy
import skimage.transform as trfm
import tifffile as tiff

from cell_tracking_BC.OLD.in_out.graphics.dbe.matplotlib.style import (
    CellAnnotationStyle,
)
from cell_tracking_BC.OLD.type.cell import state_e
from cell_tracking_BC.OLD.type.sequence import sequence_t


def SaveSequenceAnnotations(
    sequence: sequence_t,
    folder: path_t,
    file: Union[str, path_t],
    /,
    *,
    cell_margin: float = -50.0,
) -> None:
    """"""
    track_labels = {_tpt: {} for _tpt in range(sequence.length)}
    for track in sequence.tracks:
        root_time_point = track.CellTimePoint(track.geometric_root)
        for path, label in track.LabeledSinglePathIterator(topologic_mode=True):
            for time_point, cell in enumerate(path, start=root_time_point):
                if cell.state is state_e.pruned:
                    text = (
                        f"{label}-"  # Leave "-" at the end to allow numerical sorting
                    )
                elif cell.state is state_e.dead:
                    text = (
                        f"{label}x"  # Leave "x" at the end to allow numerical sorting
                    )
                elif cell.state is state_e.dividing:
                    text = (
                        f"{label}y"  # Leave "x" at the end to allow numerical sorting
                    )
                else:
                    text = str(label)
                if cell in track_labels[time_point]:
                    track_labels[time_point][cell][0].append(text)
                else:
                    track_labels[time_point][cell] = ([text], cell.centroid)

    backend = pypl.get_backend()
    pypl.switch_backend("Agg")
    figure, axes = pypl.subplots(facecolor="w")
    canvas = figure.canvas
    renderer = canvas.get_renderer()

    annotated = None
    frame_shape = sequence.cell_frames[0].shape
    for f_idx, frame in enumerate(sequence.cell_frames):
        if f_idx % 20 == 0:
            print(f"    Writing frame {f_idx} @ {time.ctime()}...")

        axes.clear()
        axes.set_xlim(left=0, right=frame_shape[1] - 1)
        axes.set_ylim(bottom=0, top=frame_shape[0] - 1)
        axes.xaxis.set_visible(False)
        axes.yaxis.set_visible(False)
        axes.set_facecolor("k")
        axes.set_position((0.0, 0.0, 1.0, 1.0))

        description = frame.Description(margins=(0.0, cell_margin))
        # for contours in description["cell_contours"].values():
        #     axes.scatter(
        #         contours[1],
        #         contours[0],
        #         color=(0.0, 0.8, 0.8, 0.3),
        #     )
        for contours in description["cell_contours"].values():
            for contour in contours:
                axes.plot(
                    contour[:, 1],
                    contour[:, 0],
                    linestyle=":",
                    color=(0.0, 0.8, 0.8, 0.3),
                )

        # description = sequence.DescriptionOfFrame(f_idx)
        for text, position in track_labels[f_idx].values():
            text = "\n".join(sorted(text))
            additionals = CellAnnotationStyle(False, "\n" in text)
            axes.annotate(
                text,
                nmpy.flipud(position),
                ha="center",
                va="center",
                **additionals,
            )
        canvas.draw()

        content = nmpy.array(renderer.buffer_rgba())[1:, 1:, :3]
        if annotated is None:
            annotated = nmpy.empty((*content.shape, sequence.length), dtype=nmpy.uint8)
        annotated[..., f_idx] = content

    pypl.close(fig=figure)  # To prevent remaining caught in event loop
    pypl.switch_backend(backend)

    # row_slice, col_slice = BoundingBoxSlices(annotated)
    # annotated = annotated[row_slice, col_slice, :, :]
    annotated = trfm.resize(
        annotated, (*sequence.shape, 3, sequence.length), preserve_range=True
    )
    annotated = annotated.astype(nmpy.uint8, copy=False)
    annotated = nmpy.moveaxis(annotated, (0, 1, 2, 3), (2, 3, 1, 0))
    annotated = annotated[:, nmpy.newaxis, :, :, :]

    tiff.imwrite(
        str(folder / file),
        annotated,
        photometric="rgb",
        compression="deflate",
        planarconfig="separate",
        metadata={"axes": "XYZCT"},
    )
