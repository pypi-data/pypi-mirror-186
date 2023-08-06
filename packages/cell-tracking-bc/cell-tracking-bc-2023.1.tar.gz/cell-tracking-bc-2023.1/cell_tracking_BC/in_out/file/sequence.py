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

from pathlib import Path as path_t
from typing import Callable, Sequence, Union

import imageio as mgio
import mrc as mrci
import numpy as nmpy
import tifffile as tiff

import cell_tracking_BC.in_out.file.frame as frio


array_t = nmpy.ndarray


# TODO: check the output format of the different functions. In particular, do they all output the time dimension as the
#       last one?
# TODO: Probably add (generic) parameters to specify eventual required hints for reading function such as number of
#       channels...


def SequenceByITK(path: path_t, /) -> array_t:
    """
    Shape: time*channel x row x col
    """
    return frio.FrameByITK(path)


def SequenceByIMAGEIO(path: path_t, /) -> array_t:
    """"""
    return mgio.volread(path)


def SequenceFromPath(
    path: path_t,
    /,
    *,
    SequenceLoading: Callable[[path_t], array_t] = SequenceByIMAGEIO,
) -> array_t:
    """"""
    # TODO: make this function work in "every" cases (add a parameter about expected dimension arrangements), or
    #       remove the sequence loading functionality from cell-tracking-bc, leaving this task to the end user.
    if not (path.exists() and path.is_file()):
        raise ValueError(f"{path}: Not a path to an existing file")

    if (img_format := path.suffix[1:].lower()) in ("tif", "tiff"):
        output = tiff.imread(str(path))
    elif img_format in ("dv", "mrc"):
        # numpy.array: Because the returned value seems to be a read-only memory map
        output = nmpy.array(mrci.imread(str(path)))
        if output.ndim == 5:
            # Probably: time x channel x Z x Y x X while sequences are time x channel x (Z=1 x) Y x X, so one gets:
            # time x channel=1 x Z=actual channels x Y x X
            output = output[:, 0, :, :]
    else:
        output = SequenceLoading(path)

    return output


def SaveSequenceAsTIFF(
    sequence: Union[array_t, Sequence[array_t]], path: Union[str, path_t], /
) -> None:
    """"""
    if isinstance(sequence, array_t):
        volume = sequence
    else:
        volume = nmpy.dstack(sequence)

    tiff.imwrite(
        str(path),
        volume,
        photometric="rgb",
        compression="deflate",
        planarconfig="separate",
        metadata={"axes": "XYZCT"},
    )
