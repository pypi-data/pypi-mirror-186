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
from typing import Any, Optional, Sequence, Tuple, Union

import numpy as nmpy
import scipy.ndimage as ndimage_t

import json_any.json_any as jsnr
from cell_tracking_BC.OLD.type.compartment import compartment_t
from cell_tracking_BC.OLD.type.cytoplasm import cytoplasm_t
from cell_tracking_BC.OLD.type.nucleus import nucleus_t


array_t = nmpy.ndarray
nucleus_or_nuclei_h = Union[nucleus_t, Tuple[nucleus_t, nucleus_t]]


class state_e(enum_t):
    unknown = None
    pruned = -1
    living = 1
    dividing = 2
    dead = 0

    def IsActive(self, /, *, strict_mode: bool = False) -> bool:
        """"""
        if strict_mode:
            return self not in (state_e.dead, state_e.pruned, state_e.unknown)

        return self not in (state_e.dead, state_e.pruned)

    def IsAlive(self, /, *, strict_mode: bool = False) -> bool:
        """"""
        if strict_mode:
            return self in (state_e.living, state_e.dividing)

        return self in (state_e.living, state_e.dividing, state_e.unknown)


@dtcl.dataclass(repr=False, eq=False)
class cell_t(compartment_t):

    label: Any = None
    nucleus: Optional[nucleus_or_nuclei_h] = None
    cytoplasm: Optional[cytoplasm_t] = None
    # Inherited from compartment_t (among others): features
    state: state_e = state_e.unknown

    @classmethod
    def NewFromMap(cls, _: array_t, /, *, is_plain: bool = True) -> compartment_t:
        """"""
        raise RuntimeError(
            f"{cell_t.NewFromMap.__name__}: Not meant to be called from class {cell_t.__name__}; "
            f"Use {cell_t.NewFromMaps.__name__} instead"
        )

    @classmethod
    def NewFromMaps(
        cls,
        label: Any,
        /,
        *,
        cell_map: array_t = None,
        cytoplasm_map: array_t = None,
        nucleus_map: array_t = None,
        safe_mode: bool = True,
    ) -> cell_t:
        """
        cell_map: Defined optional to follow cytoplasm and nucleus, but never None in fact
        Valid options: see CellAndCytoplasmMapsFromCombinations
        """
        if safe_mode:
            cell_map, cytoplasm_map, nucleus_map = CellAndCytoplasmMapsFromCombinations(
                cell=cell_map,
                cytoplasm=cytoplasm_map,
                nucleus=nucleus_map,
                should_return_nucleus=True,
            )
        cell = compartment_t.NewFromMap(cell_map)
        if cytoplasm_map is None:
            cytoplasm = None
        else:
            cytoplasm = cytoplasm_t.NewFromMap(cytoplasm_map, is_plain=False)
        if nucleus_map is None:
            nucleus = None
        else:
            nucleus = nucleus_t.NewFromMap(nucleus_map)

        instance = cls(
            label=label,
            nucleus=nucleus,
            cytoplasm=cytoplasm,
            centroid=cell.centroid,
            bb_slices=cell.bb_slices,
            touches_border=cell.touches_border,
            map_stream=cell.map_stream,
            area=cell.area,
        )

        return instance

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> cell_t:
        """"""
        return jsnr.ObjectFromJsonString(
            jsoned,
            builders={cls.__name__: cls.NewFromJsonDescription, "state_e": state_e},
        )

    def AddNucleus(self, nucleus_map: array_t, /) -> None:
        """
        For dividing cells
        """
        if self.nucleus is None:
            raise RuntimeError(f"Cannot add nucleus to a cell without a nucleus yet")

        nucleus = nucleus_t.NewFromMap(nucleus_map)
        self.nucleus = (self.nucleus, nucleus)

    @property
    def nuclei(self) -> Tuple[nucleus_t, ...]:
        """"""
        if self.nucleus is None:
            output = ()
        elif isinstance(self.nucleus, nucleus_t):
            output = (self.nucleus,)
        else:
            output = self.nucleus

        return output

    def Map(
        self,
        shape: Sequence[int],
        /,
        *,
        as_boolean: bool = False,
        with_labels: bool = False,
        margin: float = None,
    ) -> array_t:
        """
        with_labels: cytoplasm will be marked with label 1, nuclei with subsequent labels
        /!\ If with_labels, no margin should be requested. Indeed, what should be done with the nucleus map then?
        Apply the same margin or not? Or the method should take an additional margin parameter for the nucleus.
        """
        output = super().Map(shape, as_boolean=as_boolean, margin=margin)

        if with_labels:
            if as_boolean:
                raise ValueError('"with_labels" and "as_boolean" cannot be both True')

            if self.nucleus is not None:
                if isinstance(self.nucleus, nucleus_t):
                    nuclei = (self.nucleus,)
                else:
                    nuclei = self.nucleus
                for n_idx, nucleus in enumerate(nuclei, start=2):
                    map_ = nucleus.Map(shape, as_boolean=True)
                    output[map_] = n_idx

        return output

    def __str__(self) -> str:
        """"""
        super_str = super().__str__()

        lines = [super_str, "--- With compartments:"]
        initial_n_lines = lines.__len__()
        for compartment in (*self.nuclei, self.cytoplasm):
            if compartment is not None:
                lines.append(str(compartment))
        if lines.__len__() == initial_n_lines:
            return super_str

        return "\n".join(lines)


def CellAndCytoplasmMapsFromCombinations(
    *,
    cell: array_t = None,
    cytoplasm: array_t = None,
    nucleus: array_t = None,
    should_return_nucleus: bool = False,
) -> Union[Tuple[array_t, array_t], Tuple[array_t, array_t, array_t]]:
    """
    Valid options:
        - cell               => cytoplasm = None, nucleus = None
        - cell, cytoplasm    => nucleus = cell - cytoplasm
        - cell, nucleus      => cytoplasm = cell - nucleus
        - cytoplasm          => cell = filled cytoplasm, nucleus = cell - cytoplasm
        - cytoplasm, nucleus => cell = cytoplasm + nucleus
    """
    if cell is not None:
        cell = cell > 0
    if cytoplasm is not None:
        cytoplasm = cytoplasm > 0
    if nucleus is not None:
        nucleus = nucleus > 0
    filled_cytoplasm = None

    if (cell is None) and (cytoplasm is None):
        raise ValueError("Cytoplasm and cell arrays both None")
    if not ((cell is None) or (cytoplasm is None) or (nucleus is None)):
        raise ValueError("Nucleus, cytoplasm and cell arrays all not None")

    if not ((cell is None) or (cytoplasm is None)):
        filled_cytoplasm = ndimage_t.binary_fill_holes(cytoplasm)
        if not nmpy.array_equal(filled_cytoplasm, cell):
            raise ValueError("Cytoplasm outer borders do not coincide with cells")
    if not ((cell is None) or (nucleus is None)):
        if nmpy.any(cell[nucleus] == False):
            raise ValueError("Nuclei outer borders not restricted to cells")
    if not ((cytoplasm is None) or (nucleus is None)):
        if nmpy.any(cytoplasm[nucleus]):
            raise ValueError("Cytoplasm and nucleus arrays intersect")
        # Necessarily not already computed above since all 3 segmentations cannot be passed
        filled_cytoplasm = ndimage_t.binary_fill_holes(cytoplasm)
        union = nmpy.logical_or(cytoplasm, nucleus)
        if not nmpy.array_equal(filled_cytoplasm, union):
            raise ValueError("Cytoplasm inner borders do not coincide with nuclei")

    if cell is None:  # Then cytoplasm is not None
        if filled_cytoplasm is None:
            if nucleus is None:
                cell = ndimage_t.binary_fill_holes(cytoplasm)
            else:
                cell = cytoplasm.copy()
                cell[nucleus] = True
        else:
            cell = filled_cytoplasm
    # From then on, cell is not None

    if (cytoplasm is None) and (nucleus is not None):
        cytoplasm = cell.copy()
        cytoplasm[nucleus] = False
    if cytoplasm is not None:
        if filled_cytoplasm is None:
            filled_cytoplasm = ndimage_t.binary_fill_holes(cytoplasm)
        if nucleus is None:
            nucleus = filled_cytoplasm.copy()
            nucleus[cytoplasm] = False

        cytoplasms, n_cytoplasms = ndimage_t.label(filled_cytoplasm)  # connectivity=1
        nuclei, _ = ndimage_t.label(nucleus)  # connectivity=1
        for label in range(1, n_cytoplasms + 1):
            labels_inside = nmpy.unique(nuclei[cytoplasms == label])
            n_nuclei = labels_inside[labels_inside > 0].size
            if (n_nuclei < 1) or (n_nuclei > 2):
                raise ValueError(
                    f"{n_nuclei}: Invalid number of nuclei in cytoplasm. Expected=1 or 2."
                )

    if should_return_nucleus:
        if (nucleus is None) and (cytoplasm is not None):
            if filled_cytoplasm is None:
                filled_cytoplasm = ndimage_t.binary_fill_holes(cytoplasm)
            nucleus = filled_cytoplasm.copy()
            nucleus[cytoplasm] = False

        return cell, cytoplasm, nucleus

    return cell, cytoplasm
