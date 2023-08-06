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
from enum import Enum as enum_t
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import numpy as nmpy

# import scipy.ndimage as spim
# import scipy.optimize as spop
import skimage.morphology as mrph

# import skimage.segmentation as sgmt
from scipy.sparse import csr_array as s_array_t

# from scipy.spatial import distance as dstc

# import cell_tracking_BC.task.registration as rgst
# from cell_tracking_BC.in_out.text.logger import LOGGER
# from cell_tracking_BC.task.jaccard import PseudoJaccard
from cell_tracking_BC.type.compartment.cell import cell_t


array_t = nmpy.ndarray


class compartment_t(enum_t):
    CELL = 0
    CYTOPLASM = 1
    NUCLEUS = 2


_CELL_IDX = compartment_t.CELL.value
_CYTO_IDX = compartment_t.CYTOPLASM.value


frame_h = s_array_t
version_id_h = Tuple[int, str]
versioned_compartment_h = Union[frame_h, None, version_id_h]
version_h = Tuple[versioned_compartment_h, versioned_compartment_h]
versions_h = Dict[version_id_h, version_h]
inner_outer_associations_h = Dict[int, Union[int, Tuple[int, int]]]

CellIssues_h = Callable[[int, array_t, dict], Optional[Union[str, Sequence[str]]]]


AsArray = s_array_t.toarray


@dtcl.dataclass(repr=False, eq=False)
class segmentation_t:

    shape: Tuple[int, int] = None
    cell: frame_h = None  # dtype=bool; Never None after instantiation
    # Storing the cytoplasm map preferably to nucleus map since it is easier to modify in coherence with the cell map
    # (1-to-1 correspondance and same outer border).
    cytoplasm: frame_h = None  # dtype=bool
    version_idx: int = 0
    version_name: str = "original"
    # version: See property "version"
    versions: versions_h = dtcl.field(init=False, default_factory=dict)
    cells: List[cell_t] = dtcl.field(init=False, default_factory=list)
    invalid_cells: List[Tuple[int, Union[str, Sequence[str]]]] = dtcl.field(
        init=False, default_factory=list
    )

    def __post_init__(self) -> None:
        """"""
        version = self._NewVersionFromCompartments(self.cell, self.cytoplasm)
        self.versions[self.version] = version

    @classmethod
    def NewFromCompartments(
        cls,
        cell: array_t,
        /,
        *,
        cytoplasm: array_t = None,
    ) -> segmentation_t:
        """"""
        shape = cell.shape
        cell = s_array_t(cell)
        if cytoplasm is not None:
            cytoplasm = s_array_t(cytoplasm)

        return cls(shape=shape, cell=cell, cytoplasm=cytoplasm)

    def AddFakeVersion(self, version: str, /) -> None:
        """"""
        self._AddVersionForCompartments(
            self.cell, self.cytoplasm, version, (False, False)
        )

    def _AddVersionForCompartments(
        self,
        cell: frame_h,
        cytoplasm: Optional[frame_h],
        version: str,
        has_changed: Tuple[bool, bool],
        /,
    ) -> None:
        """
        Cell and cytoplasm are supposed to already be in their most concise format
        """
        if has_changed[0]:
            self.cell = cell
        else:
            cell = self.version
        if has_changed[1]:
            self.cytoplasm = cytoplasm
        else:
            cytoplasm = self.version
        new_version = self._NewVersionFromCompartments(cell, cytoplasm)

        self.version_idx += 1
        self.version_name = version
        self.versions[self.version] = new_version

    def _NewVersionFromCompartments(
        self,
        cell: Union[frame_h, version_id_h],
        cytoplasm: Optional[Union[frame_h, version_id_h]],
        /,
    ) -> version_h:
        """"""
        output = [None, None]

        if IsVersion(cell):
            cell = self._ActualOriginal(cell, _CELL_IDX)
        if IsVersion(cytoplasm):
            cytoplasm = self._ActualOriginal(cytoplasm, _CYTO_IDX)

        output[_CELL_IDX] = cell
        output[_CYTO_IDX] = cytoplasm

        return output[0], output[1]

    def _ActualOriginal(self, version: version_id_h, index: int, /) -> version_id_h:
        """"""
        output = version

        while IsVersion(self.versions[output][index]):
            output = self.versions[output][index]

        return output

    @property
    def available_versions(
        self,
    ) -> Tuple[Tuple[compartment_t, ...], Sequence[version_id_h]]:
        """
        The sequences contain tuples (version index, version basename, version name), where version name is a
        combination of version index and basename.
        """
        if self.cytoplasm is None:
            compartments = (compartment_t.CELL,)
        else:
            compartments = (
                compartment_t.CELL,
                compartment_t.CYTOPLASM,
                compartment_t.NUCLEUS,
            )

        versions = []
        for version in self.versions.keys():
            versions.append(version)

        return compartments, versions

    @property
    def version(self) -> version_id_h:
        """"""
        return self.version_idx, self.version_name

    @property
    def nucleus(self) -> array_t:
        """"""
        if self.cytoplasm is None:
            raise RuntimeError(
                "Requesting nucleus map in a segmentation w/o cytoplasm map"
            )

        output = AsArray(self.cell)
        output[AsArray(self.cytoplasm)] = False

        return output

    def LatestCompartment(self, compartment: compartment_t, /) -> array_t:
        """"""
        if compartment is compartment_t.CELL:
            return AsArray(self.cell)

        if compartment is compartment_t.CYTOPLASM:
            if self.cytoplasm is not None:
                return AsArray(self.cytoplasm)
        elif compartment is compartment_t.NUCLEUS:
            return self.nucleus

        raise ValueError(f"{compartment}: Invalid compartment, or compartment is None")

    def CompartmentWithVersion(
        self, compartment: compartment_t, /, *, index: int = None, name: str = None
    ) -> array_t:
        """
        index: if None and name is None also, then returns latest version
        """
        if (
            ((index is None) and (name is None))
            or (index == self.version_idx)
            or (name == self.version_name)
        ):
            return self.LatestCompartment(compartment)

        if index is None:
            VersionIsAMatch = lambda _ver: name == _ver[1]
        elif name is None:
            VersionIsAMatch = lambda _ver: index == _ver[0]
        else:
            VersionIsAMatch = lambda _ver: (index, name) == _ver
        for version in self.versions.keys():
            if VersionIsAMatch(version):
                output = self._ResolvedCompartmentWithVersion(compartment, version)
                if output is None:
                    break
                else:
                    return output

        raise ValueError(
            f"{compartment}/{index}/{name}: Invalid compartment/index/name combination"
        )

    def _ResolvedCompartmentWithVersion(
        self, compartment: compartment_t, version: version_id_h, /
    ) -> Optional[array_t]:
        """"""
        if compartment is compartment_t.NUCLEUS:
            if self.cytoplasm is None:
                output = None
            else:
                cell = self.versions[version][_CELL_IDX]
                cytoplasm = self.versions[version][_CYTO_IDX]
                if IsVersion(cell):
                    cell = self.versions[cell][_CELL_IDX]
                if IsVersion(cytoplasm):
                    cytoplasm = self.versions[cytoplasm][_CYTO_IDX]
                output = AsArray(cell)
                output[AsArray(cytoplasm)] = False
        else:
            output = self.versions[version][compartment.value]
            if IsVersion(output):
                output = self.versions[output][compartment.value]
            output = AsArray(output)

        return output

    # def NonNoneAsList(self) -> Tuple[List[array_t], Sequence[str]]:
    #     """
    #     For preparing calls to cell_tracking_BC.type.cell_t.NewFromMaps
    #     """
    #     if self.cytoplasm is None:
    #         segmentations = [AsArray(self.cell)]
    #         parameters = ("cell_map",)
    #     else:
    #         segmentations = [AsArray(self.cytoplasm), AsArray(self.cell)]
    #         parameters = ("cytoplasm_map", "cell_map")
    #
    #     return segmentations, parameters

    # def ClearBorderObjects(self) -> None:
    #     """"""
    #     if self.cytoplasm is None:
    #         originals = (AsArray(self.cell),)
    #     else:
    #         originals = (AsArray(self.cytoplasm), AsArray(self.cell))
    #     new_version = [_cpt.copy() for _cpt in originals]
    #
    #     # --- Clear outer segmentation border objects
    #     has_changed = _ClearBorderObjects(new_version, originals, -1)
    #     if more_than_1 := (new_version.__len__() > 1):
    #         # --- Clear inner segmentation border objects
    #         has_changed |= _ClearBorderObjects(new_version, originals, 0)
    #
    #     cell = s_array_t(new_version[-1])
    #     if more_than_1:
    #         cytoplasm = s_array_t(new_version[0])
    #         has_changed = (has_changed, has_changed)
    #     else:
    #         cytoplasm = None
    #         has_changed = (has_changed, False)
    #     self._AddVersionForCompartments(cell, cytoplasm, "cleared borders", has_changed)

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
    #     kwargs: Passed to CellIsInvalid as keyword arguments
    #     """
    #     assert self.cytoplasm is None
    #
    #     cell = AsArray(self.cell)
    #
    #     labeled, n_cells = mrph.label(cell, return_num=True, connectivity=1)
    #     invalids = []
    #     for label in range(1, n_cells + 1):
    #         issues = CellIssues(label, labeled, **kwargs)
    #         if issues is not None:
    #             invalids.append((label, issues))
    #
    #     if has_changed := (invalids.__len__() > 0):
    #         for invalid in invalids:
    #             cell[labeled == invalid[0]] = 0
    #             self.invalid_cells.append(invalid)
    #
    #     self._AddVersionForCompartments(
    #         s_array_t(cell),
    #         self.cytoplasm,
    #         "filtered cells",
    #         (has_changed, False),
    #     )

    # def CorrectBasedOnTemporalCoherence(
    #     self,
    #     previous: segmentation_t,
    #     /,
    #     *,
    #     min_jaccard: float = 0.75,
    #     max_area_discrepancy: float = 0.25,
    #     min_cell_area: int = 0,
    #     time_point: int = None,
    # ) -> int:
    #     """
    #     min_jaccard: Actually, Pseudo-Jaccard
    #     """
    #     current = AsArray(self.cell)
    #     previous = AsArray(previous.cell)
    #     if self.cytoplasm is None:
    #         cytoplasm = None
    #     else:
    #         cytoplasm = AsArray(self.cytoplasm)
    #     if time_point is None:
    #         at_time_point = ""
    #     else:
    #         at_time_point = f" at time point {time_point}"
    #
    #     labeled_current, n_cells_current = mrph.label(
    #         current, return_num=True, connectivity=1
    #     )
    #     labeled_previous, n_cells_previous = mrph.label(
    #         previous, return_num=True, connectivity=1
    #     )
    #     jaccards = _PairwiseJaccards(
    #         n_cells_previous, n_cells_current, labeled_previous, labeled_current
    #     )
    #     c_to_p_links = _CurrentToPreviousLinks(jaccards, min_jaccard)
    #
    #     n_corrections = 0
    #     for label_current in range(1, n_cells_current + 1):
    #         labels_previous = c_to_p_links.get(label_current - 1)
    #         if (labels_previous is not None) and (labels_previous.__len__() > 1):
    #             labels_previous = nmpy.array(labels_previous) + 1
    #             context = f"between cells {sorted(labels_previous)} and fused cell {label_current}{at_time_point}"
    #
    #             where_fused = labeled_current == label_current
    #
    #             splitted = _SplitLabels(
    #                 where_fused,
    #                 labeled_previous,
    #                 labels_previous,
    #                 max_area_discrepancy,
    #                 min_cell_area,
    #                 context,
    #             )
    #             if splitted is None:
    #                 continue
    #
    #             frontier = nmpy.logical_and(where_fused, splitted == 0)
    #             current[frontier] = 0
    #             if cytoplasm is not None:
    #                 cytoplasm[frontier] = 0
    #             n_corrections += 1
    #
    #     if cytoplasm is not None:
    #         cytoplasm = s_array_t(cytoplasm)
    #     has_changed = n_corrections > 0
    #     self._AddVersionForCompartments(
    #         s_array_t(current),
    #         cytoplasm,
    #         "corrected w/ temp corr",
    #         (has_changed, has_changed and (cytoplasm is not None)),
    #     )
    #
    #     return n_corrections

    def BuildCellsFromMaps(self) -> None:
        """
        Segmentation are supposed to be binary (as opposed to already labeled)
        """
        cell_map = AsArray(self.cell)
        labeled_cells, n_cells = mrph.label(cell_map, return_num=True, connectivity=1)

        if self.cytoplasm is None:
            for label in range(1, n_cells + 1):
                cell = cell_t.NewFromMaps(cell_map=labeled_cells == label)
                self.cells.append(cell)
        else:
            labeled_nuclei = mrph.label(self.nucleus, connectivity=1)
            # TODO: code duplication with task>segmentation>_CorrectNumberOfNucleiPerCell
            for label in range(1, n_cells + 1):
                current_cell = labeled_cells == label
                inside_cell = labeled_nuclei[current_cell]
                labels_inside = nmpy.unique(inside_cell)
                assert labels_inside[0] == 0
                assert labels_inside.size > 1
                current_nuclei = labeled_nuclei == labels_inside[1]
                if labels_inside.size > 2:
                    for nucleus_lbl in labels_inside[2:]:
                        current_nuclei = nmpy.logical_or(
                            current_nuclei, labeled_nuclei == nucleus_lbl
                        )
                cell = cell_t.NewFromMaps(
                    cell_map=current_cell, nucleus_map=current_nuclei
                )
                self.cells.append(cell)

            # cytoplasm_map = AsArray(self.cytoplasm)
            # labeled_cytoplasms, n_cytoplasms = mrph.label(
            #     cytoplasm_map, return_num=True, connectivity=1
            # )
            #
            # n_objects_per_sgm = [n_cytoplasms, n_cells]
            # inner_label_of_outer = _InnerOuterAssociations(
            #     [labeled_cytoplasms, labeled_cells], n_objects_per_sgm
            # )
            # # TODO: really necessary? are the segmentations not checked beforehand?
            # _CheckInnerOuterAssociations(inner_label_of_outer, n_objects_per_sgm)
            #
            # for outer_label in range(1, n_objects_per_sgm[1] + 1):
            #     inner_label = inner_label_of_outer[outer_label]
            #     nucleus_map = nmpy.logical_xor(
            #         labeled_cells == outer_label, labeled_cytoplasms == inner_label
            #     )
            #     cell = cell_t.NewFromMaps(
            #         cell_map=labeled_cells == outer_label, nucleus_map=nucleus_map
            #     )
            #     # if additional_nucleus is not None:
            #     #     cell.AddNucleus(labeleds[0] == additional_nucleus)
            #     self.cells.append(cell)

        # # --- Generic inner and outer segmentation list for all options
        # non_nones, parameters = self.NonNoneAsList()
        #
        # # --- Segmentation labeling and (if needed) inner-outer label associations
        # labeleds = []
        # n_objects_per_sgm = []
        # for non_none in non_nones:
        #     labeled, n_objects = mrph.label(non_none, return_num=True, connectivity=1)
        #     labeleds.append(labeled)
        #     n_objects_per_sgm.append(n_objects)
        # if labeleds.__len__() > 1:
        #     inner_label_of_outer = _InnerOuterAssociations(labeleds, n_objects_per_sgm)
        #     _CheckInnerOuterAssociations(inner_label_of_outer, n_objects_per_sgm)
        # else:
        #     inner_label_of_outer = None
        #
        # # --- Cell creation and addition
        # for outer_label in range(1, n_objects_per_sgm[-1] + 1):
        #     if inner_label_of_outer is None:
        #         labels = (outer_label,)
        #     else:
        #         labels = (inner_label_of_outer[outer_label], outer_label)
        #     kwargs = {}
        #     additional_nucleus = None
        #     for parameter, labeled, label in zip(parameters, labeleds, labels):
        #         label: Union[int, Tuple[int, int]]
        #         if isinstance(label, int):
        #             kwargs[parameter] = labeled == label
        #         else:
        #             kwargs[parameter] = labeled == label[0]
        #             additional_nucleus = label[1]
        #     # TODO: are we sure the nucleus map contains a single connected component?
        #     cell = cell_t.NewFromMaps(**kwargs)
        #     if additional_nucleus is not None:
        #         cell.AddNucleus(labeleds[0] == additional_nucleus)
        #     self.cells.append(cell)

    @property
    def has_cells(self) -> bool:
        """"""
        return (self.cells is not None) and (self.cells.__len__() > 0)

    @property
    def available_cell_features(self) -> Sequence[str]:
        """"""
        if self.has_cells:
            one_cell = self.cells[0]

            return one_cell.available_features

        raise RuntimeError("Requesting cell features of cell-less sequence")

    @property
    def cell_areas(self) -> Sequence[int]:
        """"""
        labeled, n_cells = mrph.label(
            AsArray(self.cell), return_num=True, connectivity=1
        )
        output = tuple(
            nmpy.count_nonzero(labeled == _lbl) for _lbl in range(1, n_cells + 1)
        )

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

    def AsDict(self) -> Dict[str, Any]:
        """"""
        if isinstance(self.cell, bytes):
            cell = self.cell
        else:
            cell = self.cell.tolist()
        if self.cytoplasm is None:
            cytoplasm = None
        elif isinstance(self.cytoplasm, bytes):
            cytoplasm = self.cytoplasm
        else:
            cytoplasm = self.cytoplasm.tolist()
        output = {
            "cell": cell,
            "cytoplasm": cytoplasm,
            "version_idx": self.version_idx,
            "version_name": self.version_name,
            "versions": {},
        }

        versions = output["versions"]
        for name, values in self.versions.items():
            new_values = []
            for value in values:
                if (value is None) or isinstance(value, bytes) or IsVersion(value):
                    new_value = value
                else:
                    new_value = value.tolist()
                new_values.append(new_value)
            versions[name] = new_values

        return output

    def DifferencesWith(self, other, /) -> Sequence[str]:
        """"""
        if type(other) is type(self):
            output = []

            other_as_dict = other.AsDict()
            for name, value in self.AsDict().items():
                other_value = other_as_dict[name]
                if other_value != value:
                    output.append(f"{name}: {value} != {other_value}")

            return output

        return (f"Type: {type(self).__name__} != {type(other).__name__}",)

    def __eq__(self, other) -> bool:
        """"""
        if hasattr(other, "AsDict"):
            return self.AsDict() == other.AsDict()

        return False


def IsVersion(maybe: Any, /) -> bool:
    """"""
    return (
        isinstance(maybe, tuple)
        and (maybe.__len__() == 2)
        and isinstance(maybe[0], int)
        and isinstance(maybe[1], str)
    )


# def _ClearBorderObjects(
#     compartments: List[array_t], originals: Sequence[array_t], idx: int, /
# ) -> bool:
#     """"""
#     compartment = compartments[idx]
#     sgmt.clear_border(compartment, in_place=True)
#
#     return not nmpy.array_equal(compartment, originals[idx])


# def _PairwiseJaccards(
#     n_cells_previous: int,
#     n_cells_current: int,
#     labeled_previous: array_t,
#     labeled_current: array_t,
#     /,
# ) -> array_t:
#     """"""
#     labels_previous = nmpy.fromiter(range(1, n_cells_previous + 1), dtype=nmpy.uint64)
#     labels_current = nmpy.fromiter(range(1, n_cells_current + 1), dtype=nmpy.uint64)
#     # Note the reversed parameter order in PseudoJaccard since a fusion is a division in reversed time
#     _PseudoJaccard = lambda lbl_1, lbl_2: PseudoJaccard(
#         labeled_current, labeled_previous, lbl_2, lbl_1
#     )
#
#     output = dstc.cdist(
#         labels_previous[:, None], labels_current[:, None], metric=_PseudoJaccard
#     )
#
#     return output
#
#
# def _CurrentToPreviousLinks(
#     pairwise_jaccards: array_t, min_jaccard: float, /
# ) -> Dict[int, Sequence[int]]:
#     """"""
#     output = {}
#
#     while True:
#         row_idc, col_idc = spop.linear_sum_assignment(1.0 - pairwise_jaccards)
#         valid_idc = pairwise_jaccards[row_idc, col_idc] > min_jaccard
#         if not nmpy.any(valid_idc):
#             break
#
#         valid_row_idc = row_idc[valid_idc]
#         for key, value in zip(col_idc[valid_idc], valid_row_idc):
#             if key in output:
#                 output[key].append(value)
#             else:
#                 output[key] = [value]
#
#         pairwise_jaccards[valid_row_idc, :] = 0.0
#
#     return output
#
#
# def _SplitLabels(
#     where_fused: array_t,
#     labeled_previous: array_t,
#     labels_previous: array_t,
#     max_area_discrepancy: float,
#     min_cell_area: int,
#     context: str,
#     /,
# ) -> Optional[array_t]:
#     """"""
#     output = nmpy.zeros_like(labeled_previous)
#     for l_idx, previous_label in enumerate(labels_previous, start=1):
#         output[labeled_previous == previous_label] = l_idx
#
#     fused_area = nmpy.count_nonzero(where_fused)
#     split_area = nmpy.count_nonzero(output)
#     discrepancy = abs(split_area - fused_area) / fused_area
#     if discrepancy > max_area_discrepancy:
#         LOGGER.warning(
#             f"Segmentation correction discarded due to high t-total-area/(t+1)-fused-area discrepancy "
#             f"{context}: "
#             f"Actual={discrepancy}. Expected<={max_area_discrepancy}."
#         )
#         return None
#
#     (fused_local, split_local), corners = rgst.InCommonNonZeroRectangles(
#         where_fused, output, for_rotation=True
#     )
#
#     angle = rgst.RotationInBinary(fused_local, split_local > 0)
#     rotated = rgst.RotatedLabeled(split_local, angle)
#
#     split_local = _DilatedWithLabelPreservation(rotated, fused_local, min_cell_area)
#     if split_local is None:
#         LOGGER.warning(
#             f"Segmentation correction discarded due to invalid split regions "
#             f"{context}"
#         )
#         return None
#
#     corner = corners[0]
#     rows_gbl, cols_gbl = nmpy.meshgrid(
#         range(corner[0], corner[0] + split_local.shape[0]),
#         range(corner[1], corner[1] + split_local.shape[1]),
#         indexing="ij",
#     )
#     rows_lcl, cols_lcl = nmpy.indices(split_local.shape)
#     valid = nmpy.logical_and(
#         nmpy.logical_and(rows_gbl >= 0, cols_gbl >= 0),
#         nmpy.logical_and(rows_gbl < output.shape[0], cols_gbl < output.shape[1]),
#     )
#     output.fill(0)
#     output[rows_gbl[valid], cols_gbl[valid]] = split_local[
#         rows_lcl[valid], cols_lcl[valid]
#     ]
#
#     return output
#
#
# def _DilatedWithLabelPreservation(
#     labeled: array_t, roi: array_t, min_cell_area: int, /
# ) -> Optional[array_t]:
#     """"""
#     output = nmpy.ones_like(labeled)
#
#     n_labels = nmpy.amax(labeled).item()
#     non_roi = nmpy.logical_not(roi)
#
#     distance_map = spim.distance_transform_edt(labeled != 1)
#     for label in range(2, n_labels + 1):
#         current_map = spim.distance_transform_edt(labeled != label)
#         closer_bmap = current_map < distance_map
#         output[closer_bmap] = label
#         distance_map[closer_bmap] = current_map[closer_bmap]
#
#     while True:
#         intermediate = nmpy.zeros_like(output)
#         for label in range(1, n_labels + 1):
#             where = output == label
#             if not nmpy.any(where):
#                 return None
#             # TODO: check how erosion behaves on image borders
#             eroded = mrph.binary_erosion(where)
#             intermediate[eroded] = label
#         nmpy.copyto(output, intermediate)
#         output[non_roi] = 0
#
#         eroded_labeled, n_eroded_labels = mrph.label(
#             output > 0, return_num=True, connectivity=1
#         )
#         areas = tuple(
#             nmpy.count_nonzero(eroded_labeled == _lbl)
#             for _lbl in range(1, n_eroded_labels + 1)
#         )
#         for label, area in enumerate(areas, start=1):
#             if area < min_cell_area:
#                 output[eroded_labeled == label] = 0
#                 n_eroded_labels -= 1
#         if n_eroded_labels == n_labels:
#             break
#
#     return output


# def _InnerOuterAssociations(
#     segmentations: List[array_t], n_objects_per_sgm: Sequence[int], /
# ) -> inner_outer_associations_h:
#     """
#     Actually, only used with [cytoplasms, cells]
#     """
#     # TODO: rename function, and probably simplify
#     output = {}
#
#     for inner_label in range(1, n_objects_per_sgm[0] + 1):
#         inner_map = segmentations[0] == inner_label
#         outer_label = nmpy.amax(segmentations[1][inner_map])
#         if outer_label == 0:
#             # TODO: can this happen? are the segmentations not checked beforehand?
#             continue
#
#         if outer_label in output:
#             raise RuntimeError(
#                 f"{outer_label}: Container compartment with more than two contained compartments: {output[outer_label]} + {inner_label}"
#             )
#         else:
#             output[outer_label] = inner_label
#
#     return output


# def _CheckInnerOuterAssociations(
#     inner_label_of_outer: inner_outer_associations_h,
#     n_objects_per_sgm: Sequence[int],
#     /,
# ) -> None:
#     """"""
#     if n_objects_per_sgm[0] != n_objects_per_sgm[1]:
#         LOGGER.warning(
#             f"Mismatch in number of segmented objects: {n_objects_per_sgm}; "
#             f"Might be due to cell divisions"
#         )
#
#     inner_labels = []
#     for label in inner_label_of_outer.values():
#         if isinstance(label, Sequence):
#             inner_labels.extend(label)
#         else:
#             inner_labels.append(label)
#     outer_labels = tuple(inner_label_of_outer.keys())
#     n_inner_labels = nmpy.unique(inner_labels).size
#     n_outer_labels = nmpy.unique(outer_labels).size
#     if (n_missing_associations := n_objects_per_sgm[0] - n_inner_labels) > 0:
#         LOGGER.error(
#             f"{n_missing_associations} inner compartment(s) not associated with outer compartments"
#         )
#     if (n_missing_associations := n_objects_per_sgm[1] - n_outer_labels) > 0:
#         LOGGER.error(
#             f"{n_missing_associations} outer compartment(s) without inner compartment(s)"
#         )
