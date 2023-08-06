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

import itertools as ittl

import matplotlib.pyplot as pypl
import numpy as nmpy

import cell_tracking_BC.OLD.type.cell as cll_
from cell_tracking_BC.OLD.type.cell import cell_t


array_t = nmpy.ndarray


shape = (100, 100)

nucleus_map = nmpy.zeros(shape, dtype=nmpy.bool_)
nucleus_map[20:28, 35:47] = True
nucleus_map[50:58, 60:72] = True

cytoplasm_map = nmpy.zeros(shape, dtype=nmpy.bool_)
cytoplasm_map[15:35, 29:55] = True
filled_cytoplasm_map = cytoplasm_map.copy()
cytoplasm_map[45:65, 54:80] = True
cytoplasm_map[nucleus_map] = False

cell_map = cytoplasm_map.copy()
cell_map[nucleus_map] = True

empty_map = nmpy.zeros_like(cell_map)

_, all_axes = pypl.subplots(ncols=3)
for axes, map_ in zip(all_axes, (cell_map, cytoplasm_map, nucleus_map)):
    axes.matshow(map_)

for maps in ittl.product((cell_map, None), (cytoplasm_map, None), (nucleus_map, None)):
    try:
        cell, cytoplasm, nucleus = maps
        validateds = cll_.CellAndCytoplasmMapsFromCombinations(
            cell=cell,
            cytoplasm=cytoplasm,
            nucleus=nucleus,
            should_return_nucleus=True,
        )
        _, all_axes = pypl.subplots(ncols=3)
        for axes, map_, validated in zip(all_axes, maps, validateds):
            if validated is None:
                axes.matshow(empty_map)
            else:
                axes.matshow(validated)
            axes.set_title(type(map_).__name__[:4])
    except ValueError as exc:
        types = tuple(type(_elm).__name__[:4] for _elm in maps)
        print(f"{types} => {exc}")

try:
    print("Filled cytoplasm map: Should raise an exception...")
    _ = cell_t.NewFromMaps(1, cytoplasm_map = filled_cytoplasm_map)
except ValueError as exc:
    print(f"    Exception: {exc}")

pypl.show()
