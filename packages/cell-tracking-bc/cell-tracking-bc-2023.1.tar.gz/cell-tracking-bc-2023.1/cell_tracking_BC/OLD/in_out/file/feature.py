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

import numbers as nmbr
import tempfile as temp
from pathlib import Path as path_t
from typing import Dict, IO, Optional, Sequence, Union

import xlsxwriter as xlsx
from xlsxwriter.format import Format as xlsx_format_t
from xlsxwriter.workbook import Workbook as workbook_t
from xlsxwriter.worksheet import Worksheet as worksheet_t

from cell_tracking_BC.OLD.in_out.text.logger import LOGGER
from cell_tracking_BC.OLD.standard.uid import AlphaColumnFromIndex
from cell_tracking_BC.OLD.type.cell import state_e
from cell_tracking_BC.OLD.type.sequence import sequence_t
from cell_tracking_BC.OLD.type.track.single import single_track_t


event_response_h = Dict[int, Optional[Sequence[float]]]
division_times_h = Dict[int, Sequence[int]]
death_time_h = Dict[int, int]


_INVALID_TRACK = "Invalid Track"
_PRUNED_TRACK = "Pruned Track"

_DASH_TYPES = (
    "solid",
    "round_dot",
    "square_dot",
    "dash",
    "dash_dot",
    "long_dash",
    "long_dash_dot",
    "long_dash_dot_dot",
)
_N_DASH_TYPES = _DASH_TYPES.__len__()


def SaveCellFeaturesToXLSX(
    path: Union[str, path_t],
    sequence: sequence_t,
    /,
    *,
    feature: Union[str, Sequence[str]] = None,
) -> None:
    """"""
    if isinstance(path, str):
        path = path_t(path)
    if feature is None:
        features = sequence.available_cell_features
    elif isinstance(feature, str):
        features = (feature,)
    else:
        features = feature

    if path.exists():
        print(f"{path}: File (or folder) already exists...")
        path = path_t(temp.mkdtemp()) / path.name
        print(f"Using {path} instead")

    workbook = xlsx.Workbook(str(path))
    csv_path = path.with_suffix(".csv")
    csv_accessor = open(csv_path, mode="w")

    pruned_format = workbook.add_format({"bg_color": "gray"})
    division_format = workbook.add_format({"bg_color": "blue"})
    death_format = workbook.add_format({"bg_color": "red"})

    for feature in features:
        _SaveCellFeature(
            feature, sequence, workbook, csv_accessor, pruned_format, division_format, death_format
        )

    workbook.close()
    csv_accessor.close()


def _SaveCellFeature(
    feature: str,
    sequence: sequence_t,
    workbook: workbook_t,
    csv_accessor: IO,
    pruned_format: Optional[xlsx_format_t],
    division_format: Optional[xlsx_format_t],
    death_format: Optional[xlsx_format_t],
    /,
) -> None:
    """"""
    if (sequence.tracks is None) or (sequence.tracks.__len__() == 0):
        LOGGER.warning(f"Sequence with no valid tracks for feature {feature}.")
        return

    evolutions = sequence.CellFeature(feature, geometric_mode = True)
    if evolutions.__len__() == 0:
        LOGGER.warn(f"{feature}: Feature without associated tracks.")
        return

    first_label = tuple(evolutions.keys())[0]
    first_feature = evolutions[first_label][1][0]
    if not isinstance(first_feature, nmbr.Number):
        feature_type = type(first_feature).__name__
        LOGGER.warn(f'Feature of type "{feature_type}": Unhandled')
        return

    sheet_name = _SheetNameFromLongName(feature)
    worksheet = workbook.add_worksheet(sheet_name)
    csv_accessor.write(f"--- Feature {feature}\n")

    max_label = max(evolutions.keys())
    labels = sequence.tracks.labels
    per_row_limits = {}
    for label in range(1, max_label + 1):
        if label not in evolutions:
            worksheet.write_string(label - 1, 0, _INVALID_TRACK)
            csv_accessor.write(f"{label}:, {_INVALID_TRACK}\n")
            continue
        if label not in labels:
            worksheet.write_string(label - 1, 0, _PRUNED_TRACK)
            csv_accessor.write(f"{label}:, {_PRUNED_TRACK}\n")
            continue

        track, evolution = evolutions[label]
        worksheet.write_row(label - 1, track._geometric_root_time_point, evolution)
        csv_accessor.write(f"{label}:," + track._geometric_root_time_point * "," + ", ".join(map(str, evolution)) + "\n")

        _SetStateBasedCellFormat(
            worksheet,
            label - 1,
            track,
            evolution,
            pruned_format,
            division_format,
            death_format,
        )

        per_row_limits[label] = (
            track._geometric_root_time_point,
            track._geometric_root_time_point + evolution.__len__() - 1,
        )
    next_available_row = max_label

    worksheet.write_string(next_available_row, 0, "END")
    next_available_row += 2  # With margin

    _AddCellStateLegend(worksheet, next_available_row, pruned_format, division_format, death_format)
    next_available_row += 3  # With margin

    if per_row_limits.__len__() > 0:
        chart = workbook.add_chart({"type": "line"})
        for l_idx, (row, (min_col, max_col)) in enumerate(per_row_limits.items()):
            min_col = AlphaColumnFromIndex(min_col)
            max_col = AlphaColumnFromIndex(max_col)
            chart.add_series(
                {
                    "name": str(row),
                    "values": f"='{sheet_name}'!${min_col}${row}:${max_col}${row}",
                    "line": {
                        "width": 1.0,
                        "dash_type": _DASH_TYPES[l_idx % _N_DASH_TYPES],
                    },
                }
            )
        worksheet.insert_chart(f"A{next_available_row}", chart)


def SaveCellEventsToXLSX(
    path: Union[str, path_t],
    sequence: sequence_t,
    /,
    *,
    division_response: str = None,
    death_response: str = None,
) -> None:
    """"""
    if isinstance(path, str):
        path = path_t(path)
    if path.exists():
        print(f"{path}: File (or folder) already exists...")
        path = path_t(temp.mkdtemp()) / path.name
        print(f"Using {path} instead")

    workbook = xlsx.Workbook(str(path))
    pruned_format = workbook.add_format({"bg_color": "gray"})
    division_format = workbook.add_format({"bg_color": "blue"})
    death_format = workbook.add_format({"bg_color": "red"})
    csv_path = path.with_suffix(".csv")
    csv_accessor = open(csv_path, mode="w")

    division_time_points = sequence.tracks.DivisionTimePoints()
    death_time_points = sequence.tracks.DeathTimePoints(
        sequence.length, with_living_leaves=True
    )
    for SaveEvents, time_point in zip(
        (_SaveDivisionEvents, _SaveDeathEvents),
        (division_time_points, death_time_points),
    ):
        SaveEvents(workbook, csv_accessor, time_point)

    n_divisions = sequence.tracks.n_dividing_cells
    _SaveEventCounts(workbook, csv_accessor, n_divisions, death_time_points)

    for event, response in zip(
        ("division", "death"), (division_response, death_response)
    ):
        if response is not None:
            _SaveEventResponse(
                event,
                workbook,
                csv_accessor,
                response,
                sequence,
                pruned_format,
                division_format,
                death_format,
            )

    workbook.close()
    csv_accessor.close()


def _SaveDivisionEvents(
    workbook: xlsx.Workbook,
    csv_accessor: IO,
    division_time_points: Optional[division_times_h],
    /,
) -> None:
    """"""
    if (division_time_points is None) or (division_time_points.__len__() == 0):
        LOGGER.warning("Division Events: No associated tracks.")
        return

    sheet_name = _SheetNameFromLongName("division times")
    worksheet = workbook.add_worksheet(sheet_name)
    csv_accessor.write("--- Division Times\n")

    max_label = max(division_time_points.keys())
    for label in range(1, max_label + 1):
        if label not in division_time_points:
            worksheet.write_string(label - 1, 0, f"{_INVALID_TRACK} or {_PRUNED_TRACK}")
            csv_accessor.write(f"{label}:, {_INVALID_TRACK} or {_PRUNED_TRACK}\n")
            continue

        time_points = division_time_points[label]
        if (time_points is None) or (time_points.__len__() == 0):
            worksheet.write_string(label - 1, 0, "No Divisions")
            csv_accessor.write(f"{label}:, No Divisions\n")
        else:
            worksheet.write_row(label - 1, 0, time_points)
            csv_accessor.write(f"{label}:," + ", ".join(map(str, time_points))+"\n")

    worksheet.write_string(max_label, 0, "END")


def _SaveDeathEvents(
    workbook: xlsx.Workbook,
    csv_accessor: IO,
    death_time_points: Optional[death_time_h], /
) -> None:
    """"""
    if (death_time_points is None) or (death_time_points.__len__() == 0):
        LOGGER.warning("Death Events: No associated tracks.")
        return

    sheet_name = _SheetNameFromLongName("death time")
    worksheet = workbook.add_worksheet(sheet_name)
    csv_accessor.write("--- Death Times\n")

    max_label = max(death_time_points.keys())
    for label in range(1, max_label + 1):
        if label not in death_time_points:
            worksheet.write_string(label - 1, 0, f"{_INVALID_TRACK} or {_PRUNED_TRACK}")
            csv_accessor.write(f"{label}:, {_INVALID_TRACK} or {_PRUNED_TRACK}\n")
            continue

        time_point = death_time_points[label]
        if time_point is None:
            worksheet.write_string(label - 1, 0, "No Death")
            csv_accessor.write(f"{label}:, No Death\n")
        else:
            worksheet.write_number(label - 1, 0, time_point)
            csv_accessor.write(f"{label}:, {time_point}\n")

    worksheet.write_string(max_label, 0, "END")


def _SaveEventCounts(
    workbook: xlsx.Workbook,
    csv_accessor: IO,
    n_divisions: int,
    death_time_points: Optional[death_time_h],
    /,
) -> None:
    """"""
    sheet_name = _SheetNameFromLongName("event counts")
    worksheet = workbook.add_worksheet(sheet_name)
    csv_accessor.write("--- Event Counts\n")

    n_deaths_pattern = 0
    n_deaths_track = 0
    if death_time_points is not None:
        for time_point in death_time_points.values():
            if time_point is not None:
                if time_point >= 0:
                    n_deaths_pattern += 1
                else:
                    n_deaths_track += 1

    for r_idx, (title, value) in enumerate(
        zip(
            ("divisions", "death (pattern)", "death (topologic)", "death"),
            (
                n_divisions,
                n_deaths_pattern,
                n_deaths_track,
                n_deaths_pattern + n_deaths_track,
            ),
        )
    ):
        worksheet.write_string(r_idx, 0, title)
        worksheet.write_number(r_idx, 1, value)
        csv_accessor.write(f"{title}, {value}\n")


def _SaveEventResponse(
    event: str,
    workbook: xlsx.Workbook,
    csv_accessor: IO,
    name: str,
    sequence: sequence_t,
    pruned_format: xlsx_format_t,
    division_format: xlsx_format_t,
    death_format: xlsx_format_t,
    /,
) -> None:
    """"""
    if (sequence.tracks is None) or (sequence.tracks.__len__() == 0):
        LOGGER.warning(
            f"Sequence with no valid tracks for {event.title()} event responses."
        )
        return
    if name not in sequence.tracks[0].features:
        LOGGER.warning(
            f"Not all tracks have {event.title()} event responses stored."
        )
        return

    sheet_name = _SheetNameFromLongName(f"{event} response")
    worksheet = workbook.add_worksheet(sheet_name)
    csv_accessor.write(f"--- {event.title()} response\n")

    responses = sequence.TrackFeature(name)
    if responses.__len__() == 0:
        LOGGER.warn(f"{event.title()} Event Responses: No associated tracks.")
        return

    max_label = max(responses.keys())
    labels = sequence.tracks.labels
    per_row_limits = {}
    for label in range(1, max_label + 1):
        if label not in responses:
            worksheet.write_string(label - 1, 0, _INVALID_TRACK)
            csv_accessor.write(f"{label}:, {_INVALID_TRACK}\n")
            continue
        if label not in labels:
            worksheet.write_string(label - 1, 0, _PRUNED_TRACK)
            csv_accessor.write(f"{label}:, {_PRUNED_TRACK}\n")
            continue

        response = responses[label]
        if response is None:
            message = "Track too Short for Valid Response"
            worksheet.write_string(label - 1, 0, message)
            csv_accessor.write(f"{label}:, {message}\n")
        else:
            track = sequence.tracks.TrackWithLabel(label, geometric_mode = True)
            worksheet.write_row(label - 1, track._geometric_root_time_point, response)
            csv_accessor.write(
                f"{label}:," + track._geometric_root_time_point * "," + ", ".join(map(str, response)) + "\n")

            _SetStateBasedCellFormat(
                worksheet,
                label - 1,
                track,
                response,
                pruned_format,
                division_format,
                death_format,
            )

            per_row_limits[label] = (
                track._geometric_root_time_point,
                track._geometric_root_time_point + response.__len__() - 1,
            )
    next_available_row = max_label

    worksheet.write_string(next_available_row, 0, "END")
    next_available_row += 2  # With margin

    _AddCellStateLegend(worksheet, next_available_row, pruned_format, division_format, death_format)
    next_available_row += 3  # With margin

    if per_row_limits.__len__() > 0:
        chart = workbook.add_chart({"type": "line"})
        for l_idx, (row, (min_col, max_col)) in enumerate(per_row_limits.items()):
            min_col = AlphaColumnFromIndex(min_col)
            max_col = AlphaColumnFromIndex(max_col)
            chart.add_series(
                {
                    "name": str(row),
                    "values": f"='{sheet_name}'!${min_col}${row}:${max_col}${row}",
                    "line": {
                        "width": 1.0,
                        "dash_type": _DASH_TYPES[l_idx % _N_DASH_TYPES],
                    },
                }
            )
        worksheet.insert_chart(f"A{next_available_row}", chart)


def _SheetNameFromLongName(name: str, /) -> str:
    """
    Sheet names cannot exceed 31 characters in length:
    xlsxwriter.exceptions.InvalidWorksheetName: Excel worksheet name 'cfp-background_over_yfp-background' must be <= 31 chars.
    """
    LIMIT = 31

    if name.__len__() <= LIMIT:
        return name

    return f"{name[:(LIMIT-3)]}..."


def _SetStateBasedCellFormat(
    worksheet: worksheet_t,
    row: int,
    track: single_track_t,
    values: Sequence,
    pruned_format: xlsx_format_t,
    division_format: xlsx_format_t,
    death_format: xlsx_format_t,
    /,
) -> None:
    """"""
    root_time_point = track._geometric_root_time_point
    for time_point, cell in enumerate(track, start=root_time_point):
        if cell.state is state_e.pruned:
            cell_format = pruned_format
        elif cell.state is state_e.dividing:
            cell_format = division_format
        elif cell.state is state_e.dead:
            cell_format = death_format
        else:
            cell_format = None

        if cell_format is not None:
            value = values[time_point - root_time_point]
            worksheet.write_number(row, time_point, value, cell_format)


def _AddCellStateLegend(
    worksheet: worksheet_t,
    row: int,
    pruned_format: Optional[xlsx_format_t],
    division_format: Optional[xlsx_format_t],
    death_format: Optional[xlsx_format_t],
    /,
) -> None:
    """"""
    for col, state, cell_format in zip(
        range(3),
        ("Dividing", "Dead", "Pruned"),
        (division_format, death_format, pruned_format),
    ):
        if cell_format is not None:
            worksheet.write_string(row, col, state, cell_format)
