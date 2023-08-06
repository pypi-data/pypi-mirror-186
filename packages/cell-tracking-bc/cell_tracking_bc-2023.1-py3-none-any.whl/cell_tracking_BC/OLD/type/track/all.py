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


from typing import Optional, Sequence, Union

from cell_tracking_BC.OLD.standard.issue import ISSUE_SEPARATOR
from cell_tracking_BC.OLD.standard.number import MAX_INT
from cell_tracking_BC.OLD.type.cell import state_e
from cell_tracking_BC.OLD.type.track.forking import forking_track_t
from cell_tracking_BC.OLD.type.track.single import single_track_t
from cell_tracking_BC.OLD.type.track.unstructured import unstructured_track_t


structured_track_h = Union[single_track_t, forking_track_t]
any_track_h = Union[unstructured_track_t, structured_track_h]


# def DivisionTimePoints(
#     dividing_cells: Sequence[Tuple[cell_t, int]], /
# ) -> Tuple[Optional[Sequence[int]], int]:
#     """"""
#     division_time_points = tuple(_elm[1] for _elm in dividing_cells)
#     if division_time_points.__len__() > 0:
#         last_div_frm = division_time_points[-1] + 1
#     else:
#         division_time_points = None  # Used to be (-1,)
#         last_div_frm = 0
#
#     return division_time_points, last_div_frm


def BasicTrackIssues(
    track: structured_track_h,
    /,
    *,
    root_time_point_interval: Optional[Sequence[Optional[int]]] = None,
    leaves_time_point_interval: Optional[Sequence[Optional[int]]] = None,
    min_duration: int = 0,
    max_n_children: int = 2,
    can_touch_border: bool = False,
) -> Optional[Sequence[str]]:
    """
    All parameters: any limit can be ignored by setting it to None
    All intervals are inclusive.
    leaf_time_point_intervals and min_lengths: first element is for the shortest branch, the second is for the longest.
        For single tracks, both are the same.
    min_duration: min edge-wise length, inclusive, of shortest single track
    max_n_children: inclusive
    """
    output = []

    if track.root.state is state_e.dead:
        output.append('Root cell has a "dead" state')

    mini, maxi = _IntervalWithDefaults(root_time_point_interval, 0, MAX_INT)
    if not (mini <= track.root_time_point <= maxi):
        output.append(
            f"{track.root_time_point}{ISSUE_SEPARATOR}Invalid root time point. Expected={mini}..{maxi}."
        )

    min_ltp = min(track.leaves_time_points)
    max_ltp = max(track.leaves_time_points)
    mini, maxi = _IntervalWithDefaults(leaves_time_point_interval, 0, MAX_INT)
    for time_point, which in zip(
        (min_ltp, max_ltp), ("shortest", "longest")
    ):
        if not (mini <= time_point <= maxi):
            output.append(
                f"{time_point}{ISSUE_SEPARATOR}Invalid leaf time point of {which} branch. Expected={mini}..{maxi}."
            )

    if track.lengths[0] < min_duration:
        output.append(
            f"{track.lengths[0]}{ISSUE_SEPARATOR}Invalid (edge-wise) length of shortest branch. Expected>={min_duration}."
        )

    if isinstance(track, forking_track_t):
        for cell in track.nodes:
            if (n_children := track.out_degree(cell)) > max_n_children:
                output.append(
                    f"C{cell.label}T{track.CellTimePoint(cell)}{ISSUE_SEPARATOR}"
                    f"{n_children} successors. Expected=0..{max_n_children}."
                )

    if not can_touch_border:
        for cell in track.cells:
            if cell.touches_border:
                output.append(
                    f"C{cell.label}T{track.CellTimePoint(cell)}{ISSUE_SEPARATOR}Touches frame border"
                )

    if output.__len__() == 0:
        output = None

    return output


def _IntervalWithDefaults(
    interval: Optional[Sequence[Optional[int]]], default_min: int, default_max: int, /
) -> Sequence[int]:
    """"""
    if interval is None:
        return default_min, default_max

    tvl_min, tvl_max = interval
    if tvl_min is None:
        tvl_min = default_min
    if tvl_max is None:
        tvl_max = default_max

    return tvl_min, tvl_max
