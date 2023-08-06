# system modules

# internal modules

# external modules
import numpy as np


def rmse(x, y, average=np.nanmean):
    """
    Root-Average-Square-Error between two series

    Args:
        x,y: the series to compare
        average (callable, optional): the averaging function. Defaults to
            :any:`numpy.nanmean`.

            .. hint::

                Use :any:`numpy.nanmedian` for the Root-Median-Square-Error.

    Returns:
        float: the Root Average Square Error
    """
    return np.sqrt(average((x - y) ** 2))


def geothmetic_meandian(x, threshold=1e-5):
    """
    Recursive averaging by arithmetic and geometric mean and median.

    Taken from XKCD: https://xkcd.com/2435/

    Args:
        x (array-like): the input data to average
        threshold (float, optional): convergence threshold

    Returns:
        float : the geothmetic meandian
    """
    mean = np.mean(x)
    if (np.std(x) / mean) < threshold:  # converges
        return mean
    return geothmetic_meandian(
        (
            mean,  # arithmetic mean
            np.prod(x) ** (1 / len(x)),  # geometric mean
            np.median(x),  # median
        )
    )
