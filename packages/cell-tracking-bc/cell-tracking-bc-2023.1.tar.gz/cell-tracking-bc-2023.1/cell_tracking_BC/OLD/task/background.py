# from typing import Tuple, Union

import numpy as nmpy

import scipy.interpolate as trpl
import skimage as skim


array_t = nmpy.ndarray


_LOCAL_HISTOGRAM_FILTER_WIDTH = 3.0
_RESCALING_FILTER_WIDTH = 9.0


def WithBackgroundSubtracted(
    image: array_t,
    segmentation: array_t,
    /,
    *,
    mode: str = None,
    dilation: int = 5,
) -> array_t:
    """
    mode: None (=mean), mean, median, interpolated
    """
    missing_map = skim.morphology.binary_dilation(
        segmentation, selem=skim.morphology.disk(dilation)
    )
    filled_map = nmpy.logical_not(missing_map)

    if (mode is None) or (mode == "mean"):
        output = image - nmpy.mean(image[filled_map])
    elif mode == "median":
        output = image - nmpy.median(image[filled_map])
    elif mode == "interpolated":
        output = image - _PChipInterpolatedBackground(image, filled_map, missing_map)
    else:
        raise NotImplementedError(
            f"{mode}: Invalid or unimplemented background subtraction mode"
        )

    output[output < 0.0] = 0.0

    # import matplotlib.pyplot as p
    # p.matshow(image), p.colorbar()
    # a=image.copy()
    # a[missing_map] = 0
    # p.matshow(a), p.colorbar()
    # p.matshow(_PChipInterpolatedBackground(image, filled_map, missing_map)), p.colorbar()
    # p.matshow(output), p.colorbar()
    # p.show()

    return output


def _PChipInterpolatedBackground(
    incomplete: array_t, filled_map: array_t, missing_map: array_t, /
) -> array_t:
    """
    Uses pchip interpolation to avoid negative values
    """
    # Since pchip works in 1-D, interpolation has to be done in 2 steps
    # Step 1: row-wise interpolation
    row_wise = nmpy.array(incomplete, dtype=nmpy.float64)

    for col in range(row_wise.shape[1]):
        old_rows = nmpy.nonzero(filled_map[:, col])[0]
        new_rows = nmpy.nonzero(missing_map[:, col])[0]

        row_wise[new_rows, col] = trpl.pchip_interpolate(
            old_rows, incomplete[old_rows, col], new_rows
        )

    # Step 2: column-wise interpolation
    col_wise = nmpy.array(incomplete, dtype=nmpy.float64)

    for row in range(col_wise.shape[0]):
        old_cols = nmpy.nonzero(filled_map[row, :])[0]
        new_cols = nmpy.nonzero(missing_map[row, :])[0]

        col_wise[row, new_cols] = trpl.pchip_interpolate(
            old_cols, incomplete[row, old_cols], new_cols
        )

    output = nmpy.array(incomplete, dtype=nmpy.float64)
    output[missing_map] = 0.5 * (row_wise[missing_map] + col_wise[missing_map])

    return output
