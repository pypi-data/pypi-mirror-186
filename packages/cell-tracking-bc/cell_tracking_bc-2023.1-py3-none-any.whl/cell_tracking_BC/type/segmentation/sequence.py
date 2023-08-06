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

import functools as fctl
from itertools import starmap, zip_longest
from multiprocessing import Pool as pool_t
from typing import Any, Callable, ClassVar, Dict, Iterator, List, Sequence, Tuple, Union

import json_any.json_any as jsnr
import numpy as nmpy
import skimage.morphology as mrph

import cell_tracking_BC.in_out.text.progress as prgs
from cell_tracking_BC.type.acquisition.frame import all_versions_h
from cell_tracking_BC.type.compartment.cell import cell_t
from cell_tracking_BC.type.segmentation.frame import (
    AsArray,
    # CellIssues_h,
    compartment_t,
    segmentation_t,
    version_id_h,
)


array_t = nmpy.ndarray
morphological_feature_computation_h = Callable[
    [cell_t, Dict[str, Any]], Union[Any, Sequence[Any]]
]
radiometric_feature_computation_h = Callable[
    [cell_t, Union[array_t, Sequence[array_t]], Dict[str, Any]],
    Union[Any, Sequence[Any]],
]


class segmentations_t(List[segmentation_t]):
    NewFromJsonString: ClassVar[
        Callable[[str], segmentations_t]
    ] = jsnr.ObjectFromJsonString

    @classmethod
    def NewFromCompartmentSequences(
        cls,
        expected_length: int,
        /,
        *,
        cells_sgms: Sequence[array_t] = None,
        cytoplasms_sgms: Sequence[array_t] = None,
    ) -> segmentations_t:
        """"""
        instance = cls()

        if cytoplasms_sgms is None:
            cytoplasms_sgms = expected_length * [None]
        all_sequences = (cells_sgms, cytoplasms_sgms)
        lengths = tuple(map(len, all_sequences))
        if any(_lgt != expected_length for _lgt in lengths):
            raise ValueError(
                f"{lengths}: Non-none sequences do not all have expected length {expected_length}"
            )

        for cell, cytoplasm in zip(*all_sequences):
            segmentation = segmentation_t.NewFromCompartments(cell, cytoplasm=cytoplasm)
            instance.append(segmentation)

        return instance

    @classmethod
    def __NewFromJsonDescription__(
        cls, description: List[segmentation_t], /
    ) -> segmentations_t:
        """"""
        return cls(description)

    def __DescriptionForJSON__(self) -> Any:
        """"""
        return list(self)

    @property
    def length(self) -> int:
        """"""
        return self.__len__()

    @property
    def available_versions(
        self,
    ) -> Tuple[Tuple[compartment_t, ...], Sequence[version_id_h]]:
        """
        See cell_tracking_BC.type.segmentation.frame.available_versions
        """
        return self[0].available_versions

    def CompartmentsWithVersion(
        self, compartment: compartment_t, /, *, index: int = None, name: str = None
    ) -> Sequence[array_t]:
        """
        index: see cell_tracking_BC.type.segmentation.frame.CompartmentWithVersion
        """
        return tuple(
            _sgm.CompartmentWithVersion(compartment, index=index, name=name)
            for _sgm in self
        )

    # def ClearBorderObjects(self) -> None:
    #     """"""
    #     for segmentation in self:
    #         segmentation.ClearBorderObjects()

    # def FilterCellsOut(
    #     self,
    #     CellIssues: CellIssues_h,
    #     /,
    #     **kwargs,
    # ) -> None:
    #     """
    #     Currently, only applicable to the cell segmentation when no other compartments are present
    #
    #     Parameters
    #     ----------
    #     CellIssues: Arguments are: cell label (from 1), labeled segmentation, and (optional) keyword arguments; Returned
    #         value can be None, an str, or a sequence of str.
    #     kwargs: Passed to CellIsInvalid as keyword arguments with "frame_idx" (from 0) automatically added
    #     """
    #     if "frame_idx" in kwargs:
    #         raise ValueError(
    #             f'{kwargs}: Parameter name "frame_idx" '
    #             f"is reserved by {segmentations_t.FilterCellsOut.__name__}"
    #         )
    #
    #     kwargs["frame_idx"] = None
    #     for f_idx, segmentation in enumerate(self):
    #         kwargs["frame_idx"] = f_idx
    #         segmentation.FilterCellsOut(CellIssues, **kwargs)

    # def CorrectBasedOnTemporalCoherence(
    #     self,
    #     /,
    #     *,
    #     min_jaccard: float = 0.75,
    #     max_area_discrepancy: float = 0.25,
    #     min_cell_area: int = 0,
    # ) -> None:
    #     """
    #     Actually, Pseudo-Jaccard
    #     """
    #     base_description = "Segmentation Correction(s) "
    #     n_corrections = 0
    #     with prgs.ProgressDesign() as progress:
    #         progress_context = prgs.progress_context_t(
    #             progress,
    #             self.__len__() - 1,
    #             first=1,
    #             description=base_description + "0",
    #         )
    #         for f_idx in progress_context.elements:
    #             n_corrections += self[f_idx].CorrectBasedOnTemporalCoherence(
    #                 self[f_idx - 1],
    #                 min_jaccard=min_jaccard,
    #                 max_area_discrepancy=max_area_discrepancy,
    #                 min_cell_area=min_cell_area,
    #                 time_point=f_idx,
    #             )
    #             progress_context.UpdateDescription(
    #                 base_description + str(n_corrections)
    #             )
    #
    #     # Otherwise, the first frame does not have the same versions as the other ones
    #     self[0].AddFakeVersion(self[1].version_name)

    def BuildCellsFromMaps(self) -> None:
        """
        Segmentation are supposed to be binary (as opposed to already labeled)
        """
        for segmentation in self:
            segmentation.BuildCellsFromMaps()

    @property
    def has_cells(self) -> bool:
        """"""
        return self[0].has_cells

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
    def cells_iterator(self) -> Iterator[Sequence[cell_t]]:
        """"""
        for segmentation in self:
            yield segmentation.cells

    def AddCellFeature(
        self,
        name: Union[str, Sequence[str]],
        Feature: Union[
            morphological_feature_computation_h, radiometric_feature_computation_h
        ],
        /,
        frames: Sequence[array_t] = None,
        should_run_in_parallel: bool = True,
        should_run_silently: bool = False,
        **kwargs,
    ) -> None:
        """
        name: If an str, then the value returned by Feature will be considered as a whole, whether it is actually a
        single value or a value container. If a sequence of str's, then the object returned by Feature will be iterated
        over, each element being matched with the corresponding name in "name".
        frames: if None, then geometrical feature, else radiometric feature.

        /!\ There is no already-existing check
        """
        if isinstance(name, str):
            description = f'Feature "{name}"'
        elif name.__len__() > 2:
            description = f'Feature "{name[0]}, ..., {name[-1]}"'
        else:
            description = f'Feature "{name[0]}, {name[1]}"'
        PreConfiguredFeatureFct = fctl.partial(Feature, **kwargs)

        with prgs.ProgressDesign(should_be_silent=should_run_silently) as progress:
            if frames is None:
                iterator = self.cells_iterator
            else:
                iterator = zip(self.cells_iterator, frames)
            progress_context = prgs.progress_context_t(
                progress,
                iterator,
                total=self.__len__(),
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

            if frames is None:
                if isinstance(name, str):
                    for cells in progress_context.elements:
                        features = MapFunctionOnList(PreConfiguredFeatureFct, cells)
                        for cell, feature in zip(cells, features):
                            cell.AddFeature(name, feature)
                else:
                    names = name
                    for cells in progress_context.elements:
                        multi_features = MapFunctionOnList(
                            PreConfiguredFeatureFct, cells
                        )
                        for cell, features in zip(cells, multi_features):
                            for name, feature in zip(names, features):
                                cell.AddFeature(name, feature)
            else:
                if isinstance(name, str):
                    for cells, frame in progress_context.elements:
                        features = StarMapFunctionOnList(
                            PreConfiguredFeatureFct,
                            zip_longest(cells, (frame,), fillvalue=frame),
                        )
                        for cell, feature in zip(cells, features):
                            cell.AddFeature(name, feature)
                else:
                    names = name
                    for cells, frame in progress_context.elements:
                        multi_features = StarMapFunctionOnList(
                            PreConfiguredFeatureFct,
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
        if self.has_cells:
            one_cell = self[0].cells[0]

            return one_cell.available_features

        raise RuntimeError("Requesting cell features of cell-less sequence")

    @property
    def cell_areas(self) -> Sequence[int]:
        """"""
        output = []

        for segmentation in self:
            labeled, n_cells = mrph.label(
                AsArray(segmentation.cell), return_num=True, connectivity=1
            )
            areas = (
                nmpy.count_nonzero(labeled == _lbl) for _lbl in range(1, n_cells + 1)
            )
            output.extend(areas)

        return output

    def CellAreaHistogram(
        self,
        /,
        *,
        n_bins: int = None,
        should_return_centers: bool = False,
        should_round_centers: bool = True,
    ) -> Tuple[array_t, array_t]:
        """"""
        areas = self.cell_areas

        if n_bins is None:
            n_bins = int(round(nmpy.sqrt(areas.__len__())))
        counts, edges = nmpy.histogram(areas, bins=n_bins)
        if should_return_centers:
            centers = 0.5 * (edges[:-1] + edges[1:])
            if should_round_centers:
                centers = nmpy.around(centers).astype(nmpy.uint64)
            edges = centers

        return counts, edges

    def __eq__(self, other) -> bool:
        """"""
        return jsnr.JsonStringOf(self) == jsnr.JsonStringOf(other)


segmentations_h = Union[Sequence[array_t], Sequence[segmentation_t], segmentations_t]


def AllSegmentations(
    segmentations: Union[Sequence[array_t], segmentations_t], /
) -> Tuple[all_versions_h, str]:
    """"""
    if isinstance(segmentations, segmentations_t):
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
        all_versions = {current_version: ((0, 1), segmentations)}

    return all_versions, current_version
