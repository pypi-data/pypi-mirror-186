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
import datetime as dttm
import shelve as shlv
import sys as sstm
from pathlib import Path as path_t
from typing import Any, Protocol, Union

import json_any.json_any as jsny
from cell_tracking_BC.OLD.in_out.text.logger import LOGGER


class jsonable_t(Protocol):
    def AsJsonString(self) -> str:
        ...

    def NewFromJsonString(self, jsoned: str, /) -> jsonable_t:
        ...


SHOULD_JSON = False
SHOULD_CHECK_JSON = False
_PIPELINE_STAGE = 0


def CacheDictionaryForMain(
    main: Union[str, path_t],
    /,
    *,
    folder_name: str = "_runtime",
    folder_postfix: str = "",
    cache_postfix: str = "",
) -> shlv.Shelf:
    """
    Call with main equal to __file__
    """
    if isinstance(main, str):
        main = path_t(main)

    cache_folder = main.parent / (folder_name + folder_postfix)
    if not cache_folder.exists():
        cache_folder.mkdir()
    elif not cache_folder.is_dir():
        print(f"{cache_folder}: Not a suitable cache folder")
        sstm.exit(-1)

    return shlv.open(str(cache_folder / (main.stem + cache_postfix)))


def CloseCache(cache: Union[shlv.Shelf, Any]) -> None:
    """"""
    if isinstance(cache, shlv.Shelf):
        cache.close()


def Save(element: jsonable_t, title: str, folder: path_t, /, **kwargs) -> None:
    """"""
    global _PIPELINE_STAGE

    if SHOULD_JSON:
        _PIPELINE_STAGE += 1
        if hasattr(element, "AsJsonString"):
            jsoned = element.AsJsonString()
        else:
            jsoned = jsny.JsonStringOf(element)
        compressed = bzp2.compress(jsoned.encode())
        with open(folder / f"{_PIPELINE_STAGE}-{title}.json", "bw") as accessor:
            accessor.write(compressed)

        if SHOULD_CHECK_JSON:
            import sys as sstm
            from json_any.test.test_json_any import DecodeAndCompare
            if not DecodeAndCompare(jsoned, element):
                sstm.exit(1)

    # import sys as sstm
    # from cell_tracking_BC.OLD.test.test_jsonization import CompareInstances
    # decoded = type(element).NewFromJsonString(jsoned)
    #
    # n_issues = CompareInstances(element, decoded)
    # if n_issues > 0:
    #     sstm.exit(1)


def Load(type_: jsonable_t, folder: path_t, /) -> object:
    """"""
    global _PIPELINE_STAGE

    _PIPELINE_STAGE += 1
    where = tuple(folder.glob(f"{_PIPELINE_STAGE}-*.json"))
    if where.__len__() != 1:
        raise RuntimeError(
            f"{folder}: Folder should contain a unique stage {_PIPELINE_STAGE}."
        )
    where = where[0]

    with open(folder / where, "br") as accessor:
        compressed = accessor.read()

    return type_.NewFromJsonString(bzp2.decompress(compressed).decode())


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
    if not output.exists():
        output.mkdir()
    elif not output.is_dir():
        print(f"{output}: Not a suitable replay folder")
        sstm.exit(-1)

    output /= folder_name
    if not output.exists():
        output.mkdir()
    elif not output.is_dir():
        print(f"{output}: Not a suitable replay folder")
        sstm.exit(-1)

    if play_date is None:
        output /= dttm.datetime.now().isoformat(timespec="milliseconds").replace(".", "-").replace(":", "-")
        if not output.exists():
            output.mkdir()
        elif not output.is_dir():
            print(f"{output}: Not a suitable replay folder")
            sstm.exit(-1)
        LOGGER.info(f"SAVING PIPELINE STAGES in subfolder {output.name}")
    elif play_date == "latest":
        everything = sorted(output.glob("*"))
        output /= everything[-1]
    else:
        output /= play_date
    if play_date is not None:
        if not output.is_dir():
            print(f"{output}: Not a valid replay folder")
            sstm.exit(-1)
        LOGGER.warn(f"REPLAYING PIPELINE from {output.name}")

    return output
