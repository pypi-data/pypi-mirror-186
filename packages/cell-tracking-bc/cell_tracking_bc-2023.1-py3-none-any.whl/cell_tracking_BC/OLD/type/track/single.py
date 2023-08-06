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
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import json_any.json_any as jsnr
from cell_tracking_BC.OLD.type.cell import cell_t, state_e
from cell_tracking_BC.OLD.type.track.structured import (
    cells_w_optional_time_points_h,
    per_single_track_cells_h,
    structured_track_t,
)


# TODO: check if grph.descendants and grph.ancestors could be used in place of more complex code here
# TODO: cell iteration methods should have a geometric_mode: bool = False parameter to allow cell-state-independent
#     iterations


class single_track_t(structured_track_t, List[cell_t]):
    label: int = None
    affinities: Tuple[float, ...] = None
    _geometric_root_time_point: int = None

    def __init__(self, *args, **kwargs) -> None:
        """"""
        list.__init__(self, *args, **kwargs)
        # Place after list init to get access to self[...]
        structured_track_t.__init__(
            self,
            root=self[0],
            leaves=(self[-1],),
        )
        self._dividing_marked = True

    @classmethod
    def NewFromOrderedCells(
        cls,
        cells: Sequence[cell_t],
        affinities: Sequence[float],
        root_time_point: int,
        label: Optional[int],
        /,
    ) -> single_track_t:
        """
        This must be the only place where direct instantiation is allowed. Anywhere else, instantiation must be
        performed with this class method.

        label: Can be None only to accommodate the creation of branches as single tracks
        """
        n_cells = cells.__len__()
        if (n_affinities := affinities.__len__()) != (n_expected := n_cells - 1):
            raise ValueError(
                f"{n_affinities}: Invalid number of affinities. Expected={n_expected}"
            )

        instance = cls(cells)
        instance.label = label
        instance.affinities = tuple(affinities)
        instance._geometric_root_time_point = root_time_point

        return instance

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> single_track_t:
        """"""
        # See NewFromJsonDescription for why builders do not count one for structured_track_t
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
    ) -> single_track_t:
        """"""
        structured, cells, attributes = description
        # See AsJsonString for why decoding happens here
        structured = structured_track_t.NewFromJsonString(structured)

        instance = cls.NewFromOrderedCells(
            cells,
            attributes["affinities"],
            attributes["_geometric_root_time_point"],
            attributes["label"],
        )

        # Do not use dtcl.asdict(self) since it recurses into dataclass instances which, if they extend a "container"
        # class like list or dict, will lose the contents.
        attributes = {
            _fld.name: getattr(structured, _fld.name)
            for _fld in dtcl.fields(structured)
        }
        for key, value in attributes.items():
            setattr(instance, key, value)

        return instance

    @property
    def cells(self) -> Union[Iterable, Iterator]:
        """"""
        return self

    @property
    def unpruned_cells(self) -> Sequence[cell_t]:
        """"""
        return self[self.index(self.root) : (self.index(self.leaves[0]) + 1)]

    # @property
    # def label(self) -> Optional[int]:
    #     """"""
    #     return self._label

    @property
    def labels(self) -> Sequence[Optional[int]]:
        """"""
        return (self.label,)  # Note: this is a tuple

    @property
    def pruned_labels(self) -> Sequence[int]:
        """"""
        if self.IsFullyPruned():
            return self.labels

        return ()

    @property
    def length(self) -> int:
        """
        Segment-wise, not node-wise
        """
        # Do not use list length as it does not account for pruned parts
        return self.lengths[0]

    @property
    def leaf(self) -> cell_t:
        """"""
        return self.leaves[0]

    @property
    def leaf_time_point(self) -> int:
        """"""
        return self.CellTimePoint(self.leaf)

    def CellTimePoint(self, cell: cell_t) -> int:
        """"""
        return self._geometric_root_time_point + self.index(cell)

    def CellSuccessors(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[cell_t]]:
        """"""
        if (not check) or (cell in self):
            where = self.index(cell)
            if where < self.__len__() - 1:
                successor = self[where + 1]
                if successor.state is state_e.pruned:
                    output = ()
                else:
                    output = (successor,)
            else:
                output = ()

            return output

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Cell not in track")

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
        if (not check) or (cell in self):
            where = self.index(cell)
            if not including_self:
                where += 1

            if where > self.__len__() - 1:
                output = ()
            else:
                output = tuple(self[where:])
                if not geometric_mode:
                    pruned = tuple(_cll.state is state_e.pruned for _cll in output)
                    if any(pruned):
                        first_pruned = pruned.index(True)
                        output = output[:first_pruned]

            return output

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Cell not in track")

    def ConfirmCellLineage(self, youngest: cell_t, oldest: cell_t, /) -> bool:
        """"""
        if (youngest in self) and (oldest in self):
            return self.index(youngest) <= self.index(oldest)

        raise ValueError(
            f"{youngest}/{oldest}: Cell track memberships={youngest in self}/{oldest in self}. "
            f"Expected=True/True"
        )

    def SplittingCells(
        self, /, *, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        return ()

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
        pass

    @property
    def n_dividing_cells(self) -> int:
        """"""
        return 0

    def DividingCells(
        self,
        /,
        *,
        with_time_point: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cells_h]:
        """"""
        if per_single_track:
            return {}
        return ()

    @property
    def unpruned_piece(self) -> single_track_t:
        """"""
        root_idx = self.index(self.root)
        leaf_idx = self.index(self.leaf)

        output = self.__class__.NewFromOrderedCells(
            self[root_idx : (leaf_idx + 1)],
            self.affinities[root_idx:leaf_idx],
            self._geometric_root_time_point + root_idx,
            self.label,
        )
        output._dead_marked = self._dead_marked

        return output

    def LabeledSinglePathIterator(
        self,
        /,
        *,
        topologic_mode: bool = False,
    ) -> Iterator[Tuple[Sequence[cell_t], int]]:
        """"""
        if topologic_mode:
            output = (self, self.label)
        else:
            output = (self.unpruned_cells, self.label)

        return iter((output,))

    @property
    def segments_iterator(self) -> Iterator[Tuple[int, cell_t, cell_t, bool]]:
        """"""
        unpruned = self.unpruned_piece

        n_cells = unpruned.__len__()
        for c_idx in range(1, n_cells):
            time_point = self.root_time_point + c_idx - 1
            is_last = c_idx == n_cells - 1
            yield time_point, *unpruned[(c_idx - 1) : (c_idx + 1)], is_last

    def PathFromTo(self, first: cell_t, last: cell_t, /) -> Sequence[cell_t]:
        """"""
        return self[self.index(first) : (self.index(last) + 1)]

    def Pieces(self, /, **_) -> Sequence[single_track_t]:
        """"""
        return (self.unpruned_piece,)  # Note: this is a tuple

    def TrackLabelsContainingCell(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[int]]:
        """
        Returns empty tuple if cell has been pruned
        """
        if (not check) or (cell in self):
            if cell.state is state_e.pruned:
                return ()
            return self.labels

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Cell not in track")

    def TrackLabelWithLeaf(
        self, leaf: cell_t, /, *, check: bool = True, tolerant_mode: bool = False, geometric_mode: bool = False,
    ) -> Optional[int]:
        """"""
        if geometric_mode:
            leaves = self.geometric_leaves
        else:
            leaves = self.leaves
        if (not check) or (leaf in leaves):
            return self.label

        if tolerant_mode:
            return None

        raise ValueError(f"{leaf}: Not a leaf cell")

    def TrackWithLeaf(
        self, leaf: cell_t, /, *, check: bool = True, tolerant_mode: bool = False,
        geometric_mode: bool = False,
    ) -> Optional[single_track_t]:
        """"""
        if geometric_mode:
            leaves = self.geometric_leaves
        else:
            leaves = self.leaves
        if (not check) or (leaf in leaves):
            if geometric_mode:
                return self
            else:
                return self.unpruned_piece

        if tolerant_mode:
            return None

        raise ValueError(f"{leaf}: Not a leaf cell")

    def AsSingleTrack(self) -> single_track_t:
        """"""
        return self.unpruned_piece

    def AsRowsColsTimes(
        self, /, *, with_labels: bool = False
    ) -> Union[
        Tuple[Tuple[float, ...], Tuple[float, ...], Tuple[int, ...]],
        Tuple[Tuple[float, ...], Tuple[float, ...], Tuple[int, ...], Tuple[int, ...]],
    ]:
        """"""
        unpruned = self.unpruned_piece
        n_cells = unpruned.__len__()

        rows, cols = tuple(zip(*(_cll.centroid.tolist() for _cll in unpruned)))
        times = tuple(range(self.root_time_point, self.root_time_point + n_cells))

        if with_labels:
            labels = tuple(_cll.label for _cll in unpruned)
            return rows, cols, times, labels

        return rows, cols, times

    def CellFeature(self, feature: str, /, *, geometric_mode: bool = False) -> Sequence[Any]:
        """
        Contrary to structured_track_t.features which are rooted at time point zero using Nones if needed, here the
        feature is returned for the unpruned part only.
        """
        if geometric_mode:
            return tuple(_cll.features[feature] for _cll in self)

        return tuple(_cll.features[feature] for _cll in self.unpruned_piece)

    def AsJsonString(self) -> str:
        """"""
        structured = structured_track_t.AsJsonString(self)
        attributes = {
            "label": self.label,
            "affinities": self.affinities,
            "_geometric_root_time_point": self._geometric_root_time_point,
        }

        # list(self): To hide this method, which would otherwise be infinitely recursively called
        return jsnr.JsonStringOf((structured, list(self), attributes), true_type=self)
