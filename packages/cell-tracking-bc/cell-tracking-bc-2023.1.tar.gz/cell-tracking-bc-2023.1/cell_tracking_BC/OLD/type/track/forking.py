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
    Callable,
    ClassVar,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import networkx as grph

import json_any.json_any as jsnr
from cell_tracking_BC.OLD.in_out.text.logger import LOGGER
from cell_tracking_BC.OLD.standard.number import INFINITY_MINUS
from cell_tracking_BC.OLD.type.cell import cell_t, state_e
from cell_tracking_BC.OLD.type.track.single import single_track_t
from cell_tracking_BC.OLD.type.track.structured import (
    PerSingleTrackCells,
    cells_w_optional_time_points_h,
    per_single_track_cells_h,
    structured_track_t,
)
from cell_tracking_BC.OLD.type.track.unstructured import TIME_POINT, unstructured_track_t


# TODO: check if grph.descendants and grph.ancestors could be used in place of more complex code here
# TODO: cell iteration methods should have a geometric_mode: bool = False parameter to allow cell-state-independent
#     iterations


# Cannot be a dataclass due to in/out_degree declarations (which are only here to silence unfound attribute warnings)
class forking_track_t(structured_track_t, grph.DiGraph):
    """
    Affinities are stored as edge attributes
    """

    SINGLE_TRACK_LABEL: ClassVar[str] = "single_track_label"

    # Mutable Tuple[List[cell_t], List[cell_t]] for without and with time points lists
    _splitting_cells_cache: List[
        Optional[List[Union[cell_t, Tuple[cell_t, int]]]]
    ] = None

    in_degree: Callable[[cell_t], int]
    out_degree: Callable[[cell_t], int]

    def __init__(
        self, track: Union[grph.DiGraph, unstructured_track_t], **kwargs
    ) -> None:
        """"""
        if isinstance(track, unstructured_track_t):
            root, _ = track.RootCellWithTimePoint()
            leaves, _ = track.LeafCellsWithTimePoints()
            structured_track_t.__init__(self, root=root, leaves=leaves)
        # /!\ Otherwise, root and leaves (and the remaining attributes of structured_track_t) must be assigned later on.
        # Use case: NewFromJsonDescription
        grph.DiGraph.__init__(self, incoming_graph_data=track, **kwargs)

    @classmethod
    def NewFromUnstructuredTrack(
        cls, track: unstructured_track_t, next_single_track_label: int, /
    ) -> Tuple[forking_track_t, int]:
        """"""
        instance = cls(track)

        for label, leaf in enumerate(instance.leaves, start=next_single_track_label):
            # Adds attribute "forking_track_t.SINGLE_TRACK_LABEL" with value "label"
            # to leaf node indexed by "leaf" (not to the leaf itself).
            grph.set_node_attributes(
                instance,
                {leaf: label},
                name=forking_track_t.SINGLE_TRACK_LABEL,
            )

        return instance, next_single_track_label + instance.n_leaves

    @classmethod
    def NewFromJsonString(
        cls,
        jsoned: str,
        /,
    ) -> forking_track_t:
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
    ) -> forking_track_t:
        """"""
        structured, graph = description
        # See AsJsonString for why decoding happens here
        structured = structured_track_t.NewFromJsonString(structured)

        instance = cls(graph)

        # Do not use dtcl.asdict(self) since it recurses into dataclass instances which, if they extend a "container"
        # class like list or dict, will lose the contents.
        attributes = {
            _fld.name: getattr(structured, _fld.name)
            for _fld in dtcl.fields(structured)
        }
        for key, value in attributes.items():
            setattr(instance, key, value)

        return instance

    def AsJsonString(self) -> str:
        """"""
        structured = structured_track_t.AsJsonString(self)

        # grph.DiGraph(self): To hide this method, which would otherwise be infinitely recursively called
        return jsnr.JsonStringOf((structured, grph.DiGraph(self)), true_type=self)

    @property
    def cells(self) -> Union[Iterable, Iterator]:
        """"""
        return self.nodes

    @property
    def label(self) -> int:
        """"""
        raise RuntimeError("A Forking track has no unique single track label")

    @property
    def labels(self) -> Sequence[int]:
        """"""
        return tuple(self.TrackLabelWithLeaf(_lef, check=False) for _lef in self.leaves)

    @property
    def pruned_labels(self) -> Sequence[int]:
        """"""
        labels = tuple(
            (self.TrackLabelWithLeaf(_lef, check=False) for _lef in _lvs)
            for _lvs in (self.geometric_leaves, self.leaves)
        )

        return tuple(set(labels[0]).difference(labels[1]))

    def LabeledSinglePathIterator(
        self,
        /,
        *,
        topologic_mode: bool = False,
    ) -> Iterator[Tuple[Sequence[cell_t], int]]:
        """"""
        if topologic_mode:
            root = self.geometric_root
            leaves = self.geometric_leaves
        else:
            root = self.root
            leaves = self.leaves
        for leaf in leaves:
            yield self.PathFromTo(root, leaf), self.TrackLabelWithLeaf(leaf, geometric_mode = topologic_mode)

    @property
    def affinities(self) -> Tuple[float, ...]:
        """"""
        output = []

        for piece in self.Pieces():
            output.extend(piece.affinities)

        return tuple(output)

    def CellTimePoint(self, cell: cell_t) -> int:
        """"""
        return self.nodes[cell][TIME_POINT]

    def CellSuccessors(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[cell_t]]:
        """"""
        if (not check) or (cell in self):
            return tuple(
                _ngh
                for _ngh in self.neighbors(cell)
                if _ngh.state is not state_e.pruned
            )

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
            output = grph.descendants(self, cell)

            if geometric_mode:
                output = tuple(output)
            else:
                output = tuple(
                    _cll for _cll in output if _cll.state is not state_e.pruned
                )

            if including_self:
                output = (cell,) + output

            return output

        if tolerant_mode:
            return None

        raise ValueError(f"{cell}: Cell not in track")

    def ConfirmCellLineage(self, youngest: cell_t, oldest: cell_t, /) -> bool:
        """"""
        if youngest is oldest:
            if youngest in self:
                return True

            raise ValueError(f"{youngest}: Cell not in track")

        if (youngest in self) and (oldest in self):
            descendants = grph.descendants(self, youngest)

            return oldest in descendants

        raise ValueError(
            f"{youngest}/{oldest}: Cell track memberships={youngest in self}/{oldest in self}. "
            f"Expected=True/True"
        )

    def SplittingCells(
        self, /, *, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        if with_time_point:
            which = 1
        else:
            which = 0
        if (self._splitting_cells_cache is None) or (
            self._splitting_cells_cache[which] is None
        ):
            if with_time_point:
                output = (
                    _rcd
                    for _rcd in self.nodes.data(TIME_POINT)
                    if self.out_degree(_rcd[0]) > 1
                )
            else:
                output = (_cll for _cll in self.nodes if self.out_degree(_cll) > 1)
            output = tuple(output)

            if self._splitting_cells_cache is None:
                self._splitting_cells_cache = [None, None]
            self._splitting_cells_cache[which] = output
        else:
            output = self._splitting_cells_cache[which]

        return output

    def MarkDividingCells(
        self,
        before_deaths: bool,
        /,
        *,
        division_responses: Dict[int, Optional[Sequence[float]]] = None,
        lower_bound: float = None,
        CombinedResponse: Callable[[Iterable], float] = max,
    ) -> None:
        """
        A division is set if the highest response at a splitting cell among the adjacent single tracks is above the
        threshold.
        """
        if before_deaths and not self._dead_marked:
            raise RuntimeError(
                'Division marking cannot be done in "before deaths" mode '
                "if dead cells have not been previously marked"
            )

        self._dividing_marked = True

        if (division_responses is None) or (lower_bound is None):
            for cell in self.SplittingCells():
                cell.state = state_e.dividing
            return

        for cell, time_point in self.SplittingCells(with_time_point=True):
            if cell.state in (state_e.dead, state_e.pruned):
                continue
            if before_deaths:
                ancestors = grph.ancestors(self, cell)
                if any(_cll.state is state_e.dead for _cll in ancestors):
                    continue

            sibling_labels = self.TrackLabelsContainingCell(cell)
            combined = CombinedResponse(
                division_responses[_lbl][time_point]
                if (division_responses[_lbl] is not None)
                and (division_responses[_lbl][time_point] is not None)
                else INFINITY_MINUS
                for _lbl in sibling_labels
            )
            if combined >= lower_bound:
                cell.state = state_e.dividing
            else:
                successors = self.CellSuccessors(cell)
                areas = tuple(_cll.area for _cll in successors)
                smallest = successors[areas.index(min(areas))]
                main_track = self.TrackLabelsContainingCell(cell)
                subtracks = self.TrackLabelsContainingCell(smallest)
                if subtracks.__len__() == 1:
                    subtracks = subtracks[0]
                LOGGER.info(
                    f"Full pruning of track {subtracks} "
                    f"(from time point {time_point + 1}) "
                    f"after splitting invalidation of track {main_track} "
                    f"at time point {time_point}"
                )
                for descendant in self.CellDescendants(smallest):
                    descendant.state = state_e.pruned
                    if descendant in self.leaves:
                        self.leaves = tuple(
                            _lef for _lef in self.leaves if _lef is not descendant
                        )

    @property
    def n_dividing_cells(self) -> int:
        """"""
        if not self._dividing_marked:
            raise RuntimeError("Dividing cells have not been marked yet")

        return sum(1 if _cll.state is state_e.dividing else 0 for _cll in self)

    def DividingCells(
        self,
        /,
        *,
        with_time_point: bool = False,
        per_single_track: bool = False,
    ) -> Union[cells_w_optional_time_points_h, per_single_track_cells_h]:
        """"""
        if not self._dividing_marked:
            raise RuntimeError("Dividing cells have not been marked yet")

        if with_time_point:
            output = (
                _rcd
                for _rcd in self.nodes.data(TIME_POINT)
                if _rcd[0].state is state_e.dividing
            )
        else:
            output = (_cll for _cll in self if _cll.state is state_e.dividing)
        # Note: PerSingleTrackCells does not accept an iterator
        output = tuple(output)

        if per_single_track:
            return PerSingleTrackCells(output, with_time_point, self)

        return output

    @property
    def segments_iterator(self) -> Iterator[Tuple[int, cell_t, cell_t, bool]]:
        """"""
        time_points = grph.get_node_attributes(self, TIME_POINT)

        for edge in self.edges:
            if all(_cll.state is not state_e.pruned for _cll in edge):
                time_point = time_points[edge[0]]
                is_last = edge[1] in self.leaves
                yield time_point, *edge, is_last

    def PathFromTo(self, first: cell_t, last: cell_t, /) -> Sequence[cell_t]:
        """"""
        return grph.shortest_path(self, source=first, target=last)

    def Pieces(
        self, /, *, from_cell: cell_t = None, with_time_point: int = None
    ) -> Sequence[single_track_t]:
        """"""
        output = []

        if from_cell is None:
            piece = [self.root]
            root_time_point = self.root_time_point
        else:
            if from_cell.state is state_e.pruned:
                raise ValueError(f"{from_cell}: Cell has been pruned")
            piece = [from_cell]
            root_time_point = with_time_point
        affinities = []

        while True:
            last_cell = piece[-1]

            if last_cell in self.leaves:
                neighbors = None
                n_neighbors = 0
            else:
                neighbors = self.CellSuccessors(last_cell, check=False)
                n_neighbors = neighbors.__len__()

            if n_neighbors == 0:
                label = self.TrackLabelWithLeaf(last_cell, check=False)
                output.append(
                    single_track_t.NewFromOrderedCells(
                        piece, affinities, root_time_point, label
                    )
                )
                break
            elif n_neighbors == 1:
                next_cell = neighbors[0]
                piece.append(next_cell)
                affinities.append(self[last_cell][next_cell]["affinity"])
            else:
                output.append(
                    single_track_t.NewFromOrderedCells(
                        piece, affinities, root_time_point, None
                    )
                )
                next_time_point = root_time_point + piece.__len__()
                for neighbor in neighbors:
                    pieces = self.Pieces(
                        from_cell=neighbor,
                        with_time_point=next_time_point,
                    )
                    for piece in pieces:
                        if piece[0] is neighbor:
                            # i.e. piece is a "root" piece, the others being located further down the subtrack tree
                            cells = (last_cell,) + tuple(piece)
                            affinity = self[last_cell][neighbor]["affinity"]
                            affinities = (affinity,) + piece.affinities
                            piece = single_track_t.NewFromOrderedCells(
                                cells,
                                affinities,
                                piece.root_time_point - 1,
                                piece.label,
                            )
                        output.append(piece)
                break

        return output

    def TrackLabelsContainingCell(
        self, cell: cell_t, /, *, check: bool = True, tolerant_mode: bool = False
    ) -> Optional[Sequence[int]]:
        """
        Returns empty tuple if cell has been pruned
        """
        if check and (cell not in self):
            if tolerant_mode:
                return None
            raise ValueError(f"{cell}: Cell not in track")

        if cell.state is state_e.pruned:
            return ()

        descendants = self.CellDescendants(cell)
        leaves = set(self.leaves).intersection(descendants)
        output = tuple(self.TrackLabelWithLeaf(_lef, check=False) for _lef in leaves)

        assert output.__len__() > 0

        return output

    def TrackLabelWithLeaf(
        self, leaf: cell_t, /, *, check: bool = True, tolerant_mode: bool = False, geometric_mode: bool = False,
    ) -> Optional[int]:
        """
        TrackLabelWithLeaf: Implicitly, it is SingleTrackLabelWithLeaf
        """
        if geometric_mode:
            leaves = self.geometric_leaves
        else:
            leaves = self.leaves
        if (not check) or (leaf in leaves):
            label = self.nodes[leaf].get(forking_track_t.SINGLE_TRACK_LABEL)
            if label is None:
                # The track has been pruned from after this "logical" leaf. All the labels of the descendant, geometric
                # leaves are therefore unused. Their minimum will be picked as the label.
                descendants = grph.descendants(self, leaf)
                geometric_leaves = set(self.geometric_leaves).intersection(descendants)
                label = min(
                    self.nodes[_lef][forking_track_t.SINGLE_TRACK_LABEL]
                    for _lef in geometric_leaves
                )

            return label

        if tolerant_mode:
            return None

        raise ValueError(f"{leaf}: Not a leaf cell")

    def TrackWithLeaf(
        self, leaf: cell_t, /, *, check: bool = True, tolerant_mode: bool = False,
        geometric_mode: bool = False,
    ) -> Optional[single_track_t]:
        """
        TrackWithLeaf: Implicitly, it is SingleTrackWithLeaf
        """
        if geometric_mode:
            leaves = self.geometric_leaves
        else:
            leaves = self.leaves
        # TODO: currently, geometric mode only accounts for leaves, not root
        if (not check) or (leaf in leaves):
            cells = grph.shortest_path(self, source=self.root, target=leaf)
            affinities = tuple(
                self[cells[_idx]][cells[_idx + 1]]["affinity"]
                for _idx in range(cells.__len__() - 1)
            )
            label = self.TrackLabelWithLeaf(leaf, check=False, geometric_mode=geometric_mode)
            output = single_track_t.NewFromOrderedCells(
                cells, affinities, self.root_time_point, label
            )

            return output

        if tolerant_mode:
            return None

        raise ValueError(f"{leaf}: Not a leaf cell")

    def AsSingleTrack(self) -> single_track_t:
        """"""
        output = [self.root]

        affinities = []
        while True:
            last_cell = output[-1]

            if last_cell in self.leaves:
                neighbors = None
                n_neighbors = 0
            else:
                neighbors = self.CellSuccessors(last_cell, check=False)
                n_neighbors = neighbors.__len__()

            if n_neighbors == 0:
                label = self.TrackLabelWithLeaf(last_cell, check=False)
                break
            elif n_neighbors == 1:
                next_cell = neighbors[0]
                output.append(next_cell)
                affinity = self[last_cell][next_cell]["affinity"]
                affinities.append(affinity)
            else:
                raise ValueError(
                    f"Attempt to convert the forking track with root {self.root} and "
                    f"{self.n_leaves} leaves into a single track"
                )

        output = single_track_t.NewFromOrderedCells(
            output, affinities, self.root_time_point, label
        )

        return output
