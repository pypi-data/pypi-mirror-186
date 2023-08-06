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

from typing import Dict, Tuple

import networkx as grph
from cell_tracking_BC.OLD.type.cell import cell_t
from cell_tracking_BC.OLD.type.track.forking import forking_track_t
from cell_tracking_BC.OLD.type.track.unstructured import unstructured_track_t


def VersionOfForkingForLayout(
    track: forking_track_t,
) -> Tuple[forking_track_t, Dict[int, cell_t]]:
    """"""
    integer_to_cell = {_key: _val for _key, _val in enumerate(track)}
    cell_to_integer = {_key: _val for _val, _key in enumerate(track)}

    unstructured = unstructured_track_t(track)
    # TODO: explain why 0 and not 1
    forking, _ = forking_track_t.NewFromUnstructuredTrack(unstructured, 0)
    grph.relabel_nodes(forking, cell_to_integer, copy=False)

    forking.root = cell_to_integer[track.root]
    forking.leaves = tuple(cell_to_integer[_lef] for _lef in track.leaves)
    forking.geometric_root = cell_to_integer[track.geometric_root]
    forking.geometric_leaves = tuple(
        cell_to_integer[_lef] for _lef in track.geometric_leaves
    )

    max_length = max(forking.lengths)
    next_idx = 0
    for single in forking.single_tracks_iterator:
        if single.length < max_length:
            n_missing = max_length - single.length
            latest_node = single[-1]
            for index in range(next_idx, next_idx + n_missing):
                new_node = f"f{index}"
                forking.add_edge(latest_node, new_node)
                latest_node = new_node
            next_idx += n_missing

    return forking, integer_to_cell
