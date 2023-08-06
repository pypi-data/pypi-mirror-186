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

import difflib as diff
from typing import Any

import numpy as nmpy

from cell_tracking_BC.OLD.type.cell import cell_t
from cell_tracking_BC.OLD.type.compartment import compartment_t
from cell_tracking_BC.OLD.type.frame import frame_t


array_t = nmpy.ndarray


def CompareInstances(element_1: Any, element_2: Any, /) -> int:
    """"""
    if element_1 == element_2:
        return 0
    else:
        if hasattr(element_1, "AsJsonString"):
            as_str = element_1.AsJsonString()
            as_str_1 = tuple(
                as_str[c_idx : (c_idx + 300)]
                for c_idx in range(0, as_str.__len__(), 300)
            )

            as_str = element_2.AsJsonString()
            as_str_2 = tuple(
                as_str[c_idx : (c_idx + 300)]
                for c_idx in range(0, as_str.__len__(), 300)
            )

            differences = "\n".join(
                diff.context_diff(as_str_1, as_str_2, fromfile="before", tofile="after")
            )
            print(f"{type(element_1).__name__}: Mismatch:\n{differences}")
        else:
            print(
                f"{type(element_1).__name__}: Mismatch:\n{element_1}\n!=\n{element_2}"
            )
        return 1


if __name__ == "__main__":
    #
    map_ = nmpy.zeros((10, 10))
    map_[4:7, 4:7] = 1

    for original in (
        compartment_t.NewFromMap(map_),
        cell_t.NewFromMaps(1, cell_map=map_),
        frame_t(map_),
    ):
        jsoned = original.AsJsonString()
        decoded = type(original).NewFromJsonString(jsoned)
        CompareInstances(original, decoded)
