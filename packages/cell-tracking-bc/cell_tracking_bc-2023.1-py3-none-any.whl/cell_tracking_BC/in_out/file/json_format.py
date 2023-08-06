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

import bz2 as bzp2
import sys as sstm
from pathlib import Path as path_t
from typing import Any, Optional, Union

import json_any.json_any as jsny
from json_any.test.test_json_any import DecodeAndCompare

import cell_tracking_BC.in_out.file.path as path
from cell_tracking_BC.in_out.text.logger import LOGGER


def Save(
    element: Any, name: str, folder: path_t, check_saving: bool, /, *, builders=None
) -> None:
    """"""
    full_name = folder / f"{name}.json"
    if full_name.exists():
        raise ValueError(f"{name}: JSON file already exists; Exiting")

    jsoned = jsny.JsonStringOf(element)
    compressed = bzp2.compress(jsoned.encode(), compresslevel=2)
    with open(full_name, "bw") as accessor:
        accessor.write(compressed)

    if check_saving:
        if hasattr(type(element), "NewFromJsonString") and hasattr(
            element, "DifferencesWith"
        ):
            decoded = type(element).NewFromJsonString(jsoned)
            differences = element.DifferencesWith(decoded)
            if differences.__len__() > 0:
                LOGGER.error("\n".join(differences))
                sstm.exit(1)
        elif not DecodeAndCompare(jsoned, element, builders=builders):
            sstm.exit(1)


def Load(
    type_: Any, name: str, folder: path_t, /, *, builders=None
) -> Optional[object]:
    """"""
    full_name = folder / f"{name}.json"
    if not full_name.is_file():
        return None

    with open(full_name, "br") as accessor:
        compressed = accessor.read()

    jsoned = bzp2.decompress(compressed).decode()

    if hasattr(type_, "NewFromJsonString"):
        return type_.NewFromJsonString(jsoned)

    return jsny.ObjectFromJsonString(jsoned, builders=builders)


def ReplayFolderForMain(
    main: Union[str, path_t],
    folder_name: str,
    /,
    *,
    base_folder_name: str = "_replay",
    base_folder_postfix: str = "",
    play_date: str = None,
) -> path_t:
    """
    Call with main equal to __file__
    play_date: Can be None (play mode), or (replay mode) "latest" or a date-time in iso format with
        timespec='milliseconds'
    """
    if isinstance(main, str):
        main = path_t(main)

    output = main.parent / (base_folder_name + base_folder_postfix)
    output = path.ReplacePathIllegalCharacters(output)
    if not output.exists():
        # exist_ok: added for thread safety (could use only mkdir then...)
        output.mkdir(exist_ok=True)
    elif not output.is_dir():
        LOGGER.error(f"{output}: Not a suitable replay folder")
        sstm.exit(-1)

    output /= path.ReplacePathIllegalCharacters(folder_name)
    if not output.exists():
        # exist_ok: added for thread safety (could use only mkdir then...)
        output.mkdir(exist_ok=True)
    elif not output.is_dir():
        LOGGER.error(f"{output}: Not a suitable replay folder")
        sstm.exit(-1)

    if play_date is None:
        output /= path.TimeStamp()
        if output.exists():
            LOGGER.error(f"{output}: Existing date-based replay folder; Exiting")
            sstm.exit(-1)
        output.mkdir()
    elif play_date == "latest":
        everything = sorted(output.glob("*"))
        output /= everything[-1]
    else:
        output /= play_date
    if play_date is not None:
        if not output.is_dir():
            LOGGER.error(f"{output}: Not a valid replay folder")
            sstm.exit(-1)

    return output
