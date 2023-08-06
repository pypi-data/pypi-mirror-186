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
from operator import itemgetter as ItemAt
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    Union,
)

import json_any.json_any as jsnr
from cell_tracking_BC.OLD.in_out.text.logger import LOGGER
from cell_tracking_BC.OLD.standard.number import INFINITY_MINUS
from cell_tracking_BC.OLD.standard.uid import Identity
from cell_tracking_BC.OLD.type.cell import cell_t, state_e


feature_filtering_h = Callable[..., Optional[Sequence[Any]]]
per_single_track_feature_h = Dict[int, Optional[Sequence[Any]]]
cells_wo_time_points = Sequence[cell_t]
cells_w_time_points_h = Sequence[Tuple[cell_t, int]]
cells_w_optional_time_points_h = Union[cells_wo_time_points, cells_w_time_points_h]
per_single_track_cells_h = Dict[int, cells_w_optional_time_points_h]
per_single_track_cell_h = Dict[int, Optional[Union[cell_t, Tuple[cell_t, int]]]]


# TODO: check if grph.descendants and grph.ancestors could be used in place of more complex code here
# TODO: cell iteration methods should have a geometric_mode: bool = False parameter to allow cell-state-independent
#     iterations


class single_additional_p(Protocol):
    label: int
    length: int

    def CellFeature(self, feature: str, /, *, geometric_mode: bool = False) -> Sequence[Any]:
        """"""

    def __getitem__(self, item):
        """"""


@dtcl.dataclass(repr=False, eq=False)
class structured_track_t:
    """
    Adding Iterable to the class inheritance silences warnings at "cell in self". Unfortunately, forking tracks become
    un-instantiable for they "lack" an __iter__ method.

    root, leaves: "logical" versions, i.e. accounting for pruning. Geometric versions are geometric_root and
    geometric_leaves.
    """

    root: cell_t = None
    leaves: Sequence[cell_t] = None
    # TODO: take advantage of these new geometric attr
    geometric_root: cell_t = dtcl.field(init=False, default=None)
    geometric_leaves: Tuple[cell_t] = dtcl.field(init=False, default=None)
    # str: feature name; int: single track label
    features: Dict[str, per_single_track_feature_h] = dtcl.field(
        init=False, default_factory=dict
    )
    _dividing_marked: bool = dtcl.field(init=False, default=False)
    _dead_marked: bool = dtcl.field(init=False, default=False)

    def __post_init__(self) -> None:
        """"""
        self.geometric_root = self.root
        self.geometric_leaves = tuple(self.leaves)

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> structured_track_t:
        """"""
        return jsnr.ObjectFromJsonString(
            jsoned,
            builders={
                cls.__name__: cls.NewFromJsonDescription,
                "cell_t": cell_t.NewFromJsonString,
            },
        )

    @classmethod
    def NewFromJsonDescription(
        cls,
        description,
        /,
    ) -> structured_track_t:
        """"""
        instance = cls.__new__(cls)
        for key, value in description.items():
            setattr(instance, key, value)

        return instance

    def AsJsonString(self) -> str:
        """"""
        # Forcing true_type guarantees that derived classes will not "cover" its value with their own type. Otherwise,
        # the decoding of a true structured_track_t instance will be incorrectly routed to the derived classes.
        return jsnr.JsonStringOf(self, true_type=structured_track_t)

    @property
    def cells(self) -> Union[Iterable, Iterator]:
        """"""
        raise NotImplementedError

    @property
    def labels(self) -> Sequence[int]:
        """
        Single track labels
        """
        raise NotImplementedError

    @property
    def labels_as_str(self) -> str:
        """
        Single track labels
        """
        return "+".join(str(_lbl) for _lbl in sorted(self.labels))

    @property
    def pruned_labels(self) -> Sequence[int]:
        """"""
        raise NotImplementedError

    @property
    def n_leaves(self) -> int:
        """"""
        return self.leaves.__len__()

    @property
    def lengths(self) -> Sequence[int]:
        """
        Segment-wise, not node-wise
        """
        return tuple(_ltp - self.root_time_point for _ltp in self.leaves_time_points)

    @property
    def root_time_point(self) -> int:
        """"""
        return self.CellTimePoint(self.root)

    @property
    def leaves_time_points(self) -> Sequence[int]:
        """"""
        return tuple(self.CellTimePoint(_lef) for _lef in self.leaves)

    def CellTimePoint(self, cell: cell_t) -> int:
        """"""
        raise NotImplementedError

    def CellSuccessors(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[cell_t]]:
        """
        Accounts for pruning
        """
        raise NotImplementedError

    def CellDescendants(
        self,
        cell: cell_t,
        /,
        *,
        including_self: bool = True,
        geometric_mode: bool = False,
        check: bool = True,
        tolerant_mode: bool = False,
    ) -> Optional[Sequence[cell_t]]:
        """"""
        raise NotImplementedError

    def ConfirmCellLineage(self, youngest: cell_t, oldest: cell_t, /) -> bool:
        """
        Including youngest is oldest
        """
        raise NotImplementedError

    def PathFromTo(self, first: cell_t, last: cell_t, /) -> Sequence[cell_t]:
        """"""
        raise NotImplementedError

    def LabeledSinglePathIterator(
        self,
        /,
        *,
        topologic_mode: bool = False,
    ) -> Iterator[Tuple[Sequence[cell_t], int]]:
        """"""
        raise NotImplementedError

    def SplittingCells(
        self, /, *, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        raise NotImplementedError

    def MarkDividingCells(
        self,
        before_deaths: bool,
        /,
        *,
        division_responses: Dict[int, Optional[Sequence[float]]] = None,
        lower_bound: float = None,
        CombinedResponse: Callable[[Iterable], float] = max,
    ) -> None:
        """"""
        raise NotImplementedError

    @property
    def n_dividing_cells(self) -> int:
        """"""
        raise NotImplementedError

    def DividingCells(
        self,
        /,
        *,
        with_time_point: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cells_h]:
        """"""
        raise NotImplementedError

    def DivisionTimePoints(self) -> Dict[int, Optional[Sequence[int]]]:
        """
        Note: There is no sense in returning not-per-single-track time points
        """
        if not self._dividing_marked:
            raise RuntimeError("Dividing cells have not been marked yet")

        dividing = self.DividingCells(with_time_point=True, per_single_track=True)

        if dividing.__len__() > 0:
            output = {
                _key: None if _val is None else tuple(map(ItemAt(1), _val))
                for _key, _val in dividing.items()
            }

            return output

        return {}  # Used to be (-1,), then None

    def MarkDeadCells(
        self,
        death_responses: Dict[int, Optional[Sequence[float]]],
        lower_bound: float,
        after_divisions: bool,
        /,
        *,
        CombinedResponse: Callable[[Iterable], float] = max,
        called_from_educated_code: bool = False,
    ) -> None:
        """
        A death is set if the highest response at a cell among the adjacent single tracks is above the threshold.

        called_from_educated_code: A track might be entirely pruned out here. Since it cannot remove itself from its
        referring objects, this method must be called from a piece of code that can do it if needed. This parameter is
        meant to prevent an "accidental" call from some "uneducated" piece of code.
        """
        if after_divisions and not self._dividing_marked:
            raise RuntimeError(
                'Death marking cannot be done in "after divisions" mode '
                "if dividing cells have not been previously marked"
            )
        if not called_from_educated_code:
            raise ValueError(
                f"{self.MarkDeadCells.__name__}: Must be called from a piece of code handling full pruning"
            )

        self._dead_marked = True

        if (death_responses is None) or (lower_bound is None):
            return

        if after_divisions:
            dividing_cells = self.DividingCells()
        else:
            dividing_cells = ()

        # This loop must not prune cells or modify leaves since it could change the sibling labels to labels of leaves
        # that have been pruned in a prior step (e.g. when validating divisions). For example, behind a cell are 2
        # leaves with labels 1 and 2. Suppose that the leaf with label 1 has been pruned in a prior step. So the cell
        # has 2 as its sibling labels. So has the cell before it. If the cell is marked dead, and the leaf with label 2
        # is pruned, the previous cell will now receive the label min(1,2), which is different from what it had.
        dead_cells = []
        for cell in self.cells:
            if cell.state in (state_e.dividing, state_e.pruned):
                continue
            if after_divisions and any(
                self.ConfirmCellLineage(cell, _dvd) for _dvd in dividing_cells
            ):
                continue

            time_point = self.CellTimePoint(cell)
            sibling_labels = self.TrackLabelsContainingCell(cell)
            combined = CombinedResponse(
                death_responses[_lbl][time_point]
                if (death_responses[_lbl] is not None)
                and (death_responses[_lbl][time_point] is not None)
                else INFINITY_MINUS
                for _lbl in sibling_labels
            )
            if combined >= lower_bound:
                # Note: The cell can be a leaf (see new_leaves below)
                dead_cells.append(cell)

        # Do not log inside the loop on dead_cells since it does not update leaves (update is done after the loop),
        # leaving the track in a transient state not suitable for TrackLabelsContainingCell.
        summary = {}
        max_time_point = self.lengths[-1]
        for cell in dead_cells:
            tracks = self.TrackLabelsContainingCell(cell)
            if tracks.__len__() == 1:
                tracks = tracks[0]
            time_point = self.CellTimePoint(cell)
            summary[tracks] = min(summary.get(tracks, max_time_point), time_point)
        for tracks, time_point in summary.items():
            LOGGER.info(
                f"Partial pruning of track {tracks} after dead cell at time point {time_point}"
            )

        invalid_leaves = []
        for cell in dead_cells:
            if cell.state is state_e.pruned:
                # It has been pruned below as a descendant
                continue

            cell.state = state_e.dead

            for descendant in self.CellDescendants(cell, including_self=False):
                descendant.state = state_e.pruned
                if descendant in self.leaves:
                    invalid_leaves.append(descendant)

        # 1. Do not use dead_cells here since it may contain dead cells after other dead cells
        # 2. Cells marked dead can already be leaves; They must not be included in new_leaves then
        new_leaves = tuple(
            _cll
            for _cll in self.cells
            if (_cll.state is state_e.dead) and (_cll not in self.leaves)
        )
        self.leaves = tuple(set(self.leaves).difference(invalid_leaves)) + new_leaves

    def DeadCells(
        self,
        sequence_length: int,
        /,
        *,
        with_time_point: bool = False,
        with_living_leaves: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cell_h]:
        """"""
        if not self._dead_marked:
            raise RuntimeError("Dead cells have not been marked yet")

        output = []

        for leaf in self.leaves:
            time_point = self.CellTimePoint(leaf)
            if (is_dead := leaf.state is state_e.dead) or (
                with_living_leaves and (time_point < sequence_length - 1)
            ):
                if with_time_point:
                    if is_dead:
                        output.append((leaf, time_point))
                    else:
                        output.append((leaf, -time_point))
                else:
                    output.append(leaf)

        if per_single_track:
            return PerSingleTrackCells(output, with_time_point, self, unique_cell=True)

        return output

    def DeathTimePoints(
        self,
        sequence_length: int,
        /,
        *,
        with_living_leaves: bool = False,
    ) -> Optional[Dict[int, Optional[int]]]:
        """
        Note: There is no sense in returning not-per-single-track time points
        """
        if not self._dead_marked:
            raise RuntimeError("Dead cells have not been marked yet")

        dead = self.DeadCells(
            sequence_length,
            with_time_point=True,
            with_living_leaves=with_living_leaves,
            per_single_track=True,
        )

        if dead.__len__() > 0:
            output = {
                _key: None if _val is None else _val[1] for _key, _val in dead.items()
            }

            return output

        return {}  # Used to be (-1,), then None

    @property
    def segments_iterator(self) -> Iterator[Tuple[int, cell_t, cell_t, bool]]:
        """"""
        raise NotImplementedError

    def Pieces(
        self, /, *, from_cell: cell_t = None, with_time_point: int = None
    ) -> Sequence[structured_track_t]:
        """"""
        raise NotImplementedError

    @property
    def single_tracks_iterator(
        self,
    ) -> Iterator[Union[structured_track_t, single_additional_p]]:
        """"""
        for leaf in self.leaves:
            yield self.TrackWithLeaf(leaf, check=False)

    @property
    def geometric_single_tracks_iterator(
        self,
    ) -> Iterator[Union[structured_track_t, single_additional_p]]:
        """"""
        for leaf in self.geometric_leaves:
            yield self.TrackWithLeaf(leaf, check=False, geometric_mode=True)

    def TrackLabelsContainingCell(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[int]]:
        """"""
        raise NotImplementedError

    def TrackLabelWithLeaf(
        self, leaf: cell_t, /, *, check: bool = True, tolerant_mode: bool = False, geometric_mode: bool = False,
    ) -> Optional[int]:
        """"""
        raise NotImplementedError

    def TrackWithLeaf(
        self,
        leaf: cell_t,
        /,
        *,
        check: bool = True,
        tolerant_mode: bool = False,
        geometric_mode: bool = False,
    ) -> Optional[structured_track_t]:
        """
        Actually, a single track
        """
        raise NotImplementedError

    def AsSingleTrack(self) -> structured_track_t:
        """"""
        raise NotImplementedError

    def IsFullyPruned(self) -> bool:
        """"""
        return self.root.state is state_e.pruned

    def AddFeature(
        self,
        name: str,
        cell_feature_names: Sequence[str],
        FeatureComputation: feature_filtering_h,
        /,
        *args,
        geometric_mode: bool = False,
        **kwargs,
    ) -> None:
        """
        /!\ There is no already-existing check
        """
        self.features[name] = {}

        per_single_track = self.features[name]
        if geometric_mode:
            iterator = self.geometric_single_tracks_iterator
        else:
            iterator = self.single_tracks_iterator
        for single in iterator:
            all_series = [single.CellFeature(_ftr, geometric_mode = geometric_mode) for _ftr in cell_feature_names]
            feature = FeatureComputation(
                *all_series, *args, track_label=single.label, **kwargs
            )
            per_single_track[single.label] = feature

    def __repr__(self) -> str:
        """"""
        return Identity(self)

    def __str__(self) -> str:
        """"""
        if hasattr(self, "nodes"):
            cells = self.nodes
        else:
            cells = self
        cell_labels = tuple(_cll.label for _cll in cells)

        return (
            f"{repr(self)}:\n"
            f"    {self.labels=}\n"
            f"    {self.root_time_point=}\n"
            f"    {self.leaves_time_points=}\n"
            f"    {self.lengths=}\n"
            f"    {cell_labels}"
        )

    def __eq__(self, other) -> bool:
        """"""
        if hasattr(other, "AsJsonString"):
            return self.AsJsonString() == other.AsJsonString()

        return False

    def __hash__(self) -> int:
        """"""
        return hash((self.root, *self.leaves))


def PerSingleTrackCells(
    linear: cells_w_optional_time_points_h,
    has_time_point: bool,
    track: structured_track_t,
    /,
    *,
    unique_cell: bool = False,
) -> Union[per_single_track_cell_h, per_single_track_cells_h]:
    """"""
    output = {}

    for single in track.single_tracks_iterator:
        if has_time_point:
            per_single = filter(lambda _rcd: _rcd[0] in single, linear)
            per_single = sorted(per_single, key=ItemAt(1))
        else:
            per_single = tuple(filter(lambda _cll: _cll in single, linear))

        if (n_cells := per_single.__len__()) > 0:
            if unique_cell:
                if n_cells > 1:
                    raise RuntimeError(
                        f"{n_cells}/{per_single}: Invalid number of cells in unique-cell mode "
                        f"for single track {single.label}"
                    )

                output[single.label] = per_single[0]
            else:
                output[single.label] = per_single
        elif unique_cell:
            output[single.label] = None
        else:
            output[single.label] = ()

    return output
