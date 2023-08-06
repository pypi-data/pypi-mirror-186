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
from typing import Callable, List, Optional, Sequence, Tuple, Union

import numpy as nmpy
import scipy.ndimage as ndimage_t
import tensorflow.keras.models as modl

import cell_tracking_BC.in_out.text.progress as prgs
from cell_tracking_BC.task.segmentation.frame import (
    AllCompartmentsFromSome as AllFrameCompartmentsFromSome,
)
from cell_tracking_BC.task.segmentation.frame import (
    CorrectBasedOnTemporalCoherence as CorrectFrameBasedOnTemporalCoherence,
)


array_t = nmpy.ndarray
processing_h = Callable[[array_t], array_t]


def SegmentationsWithTFNetwork(
    frames: Sequence[array_t],
    network_path: Union[str, path_t],
    /,
    *,
    threshold: float = 0.9,
    PreProcessed: processing_h = None,
    PostProcessed: processing_h = None,
) -> Tuple[Sequence[array_t], Sequence[array_t]]:
    """
    PostProcessed: Could be used to clear border objects. However, since one might want to segment cytoplasms and
    nuclei, clearing border objects here could lead to clearing a cytoplasm while keeping its nucleus. Consequently,
    clearing border objects here, i.e. independently for each segmentation task, is not appropriate.
    """
    output_sgm = []
    output_prd = []

    if PreProcessed is not None:
        frames = tuple(PreProcessed(_frm) for _frm in frames)
    if PostProcessed is None:
        PostProcessed = lambda _prm: _prm

    frames = nmpy.array(frames, dtype=nmpy.float32)
    if frames.ndim == 3:
        frames = nmpy.expand_dims(frames, axis=3)

    network = modl.load_model(network_path)
    # network.summary()
    predictions = network.predict(frames, verbose=1)
    # First dimension is time (needs to be removed for single frame reshape below), last dimension is channels
    # (equal to one, thus removed).
    shape = network.layers[0].input_shape[0][1:-1]

    for t_idx, prediction in enumerate(predictions):
        reshaped = nmpy.reshape(prediction, shape)
        segmentation = reshaped > threshold
        post_processed = PostProcessed(segmentation)
        if nmpy.amax(post_processed.astype(nmpy.uint8)) == 0:
            raise ValueError(f"{t_idx}: Empty segmentation")

        output_prd.append(reshaped)
        output_sgm.append(post_processed)

    return output_sgm, output_prd


def InputSizeOfTFNetwork(
    network_path: Union[str, path_t],
    /,
) -> Sequence[int]:
    """
    Input size for single frames = network input layer shape with first (time, which appears as None in network summary)
    and last dimensions (channels, but only one here) removed.
    """
    network = modl.load_model(network_path)
    layer = network.get_layer(index=0)

    return layer.input.shape[1:-1]


def FillTemporalGaps(frames: Sequence[array_t], extent: Optional[int], /) -> None:
    """"""
    if (extent is None) or (extent <= 0):
        return

    volume = nmpy.dstack(frames)
    line = nmpy.ones((1, 1, extent + 1), dtype=nmpy.bool_)
    # TODO: choose between skimage.morphology and ndimage_t versions (same remark everywhere morph. math. is used)
    ndimage_t.binary_closing(volume, structure=line, origin=(0, 0, 0), output=volume)

    # Exclude first and last frames to avoid border effects
    for f_idx in range(1, frames.__len__() - 1):
        frames[f_idx][...] = volume[..., f_idx]


def CorrectBasedOnTemporalCoherence(
    frames: Sequence[array_t],
    /,
    *,
    min_jaccard: float = 0.75,
    max_area_discrepancy: float = 0.25,
    min_cell_area: int = 0,
) -> Sequence[array_t]:
    """
    Actually, Pseudo-Jaccard
    """
    assert nmpy.issubdtype(frames[0].dtype, nmpy.bool_)

    output = frames.__len__() * [nmpy.zeros_like(frames[0])]

    base_description = "Segmentation Correction(s) "
    n_corrections = 0
    with prgs.ProgressDesign() as progress:
        progress_context = prgs.progress_context_t(
            progress,
            frames.__len__() - 1,
            first=1,
            description=base_description + "0",
        )
        for f_idx in progress_context.elements:
            n_new_corrections, output[f_idx] = CorrectFrameBasedOnTemporalCoherence(
                frames[f_idx],
                frames[f_idx - 1],
                min_jaccard=min_jaccard,
                max_area_discrepancy=max_area_discrepancy,
                min_cell_area=min_cell_area,
                time_point=f_idx,
            )
            n_corrections += n_new_corrections
            progress_context.UpdateDescription(base_description + str(n_corrections))

    # Otherwise, the first frame does not have the same versions as the other ones
    # self[0].AddFakeVersion(self[1].version_name)

    return output


def AllCompartmentsFromSome(
    length: int,
    /,
    *,
    cells_maps: List[array_t] = None,
    cytoplasms_maps: List[array_t] = None,
    nuclei_maps: List[array_t] = None,
) -> Tuple[List[array_t], List[array_t], List[array_t]]:
    """
    Valid options: see AllFrameCompartmentsFromSome
    """
    if cells_maps is None:
        cells_maps = length * [None]
    if cytoplasms_maps is None:
        cytoplasms_maps = length * [None]
    if nuclei_maps is None:
        nuclei_maps = length * [None]

    assert (
        cells_maps.__len__()
        == cytoplasms_maps.__len__()
        == nuclei_maps.__len__()
        == length
    )

    for m_idx in range(length):
        (
            cells_maps[m_idx],
            cytoplasms_maps[m_idx],
            nuclei_maps[m_idx],
        ) = AllFrameCompartmentsFromSome(
            cells_map=cells_maps[m_idx],
            cytoplasms_map=cytoplasms_maps[m_idx],
            nuclei_map=nuclei_maps[m_idx],
        )

    return cells_maps, cytoplasms_maps, nuclei_maps
