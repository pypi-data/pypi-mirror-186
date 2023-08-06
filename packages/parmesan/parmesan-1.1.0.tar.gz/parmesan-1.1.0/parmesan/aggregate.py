# system modules

# internal modules
from parmesan.accessor import ParmesanAccessor

# external modules
import numpy as np
import pandas as pd


@ParmesanAccessor.register
def temporal_cycle(x, interval, resolution, times=None, modifier=lambda x: x):
    """
    Calculate a temporal cycle

    Examples
    ========

    .. code-block:: python

        # diurnal/daily cycle
        temporal_cycle(x, interval="D", resolution="m")
        # seasonal/yearly cycle
        temporarl_cycle(x, interval="Y", resolution="D")

    Args:
        x (pandas.DataFrame or pandas.Series or numpy.ndarray): the data to
            aggregate
        times (pandas.DatetimeIndex or numpy.ndarray of datetime64, optional):
            the times to use
        interval (str, optional): the interval to aggregate to. Has to be a
            string usable with numpy.datetime64_, e.g. ``"D"`` for a diurnal
            cycle.
        resolution (str, optional): the resolution to aggregate with. Has to be
            a string usable with numpy.datetime64_, e.g. ``"s"`` for a
            resulting resolution of seconds.
        modifier (callable, optional): a callable modifying the axis to
            aggregate over. This can be used to fine-tune the output
            resolution. For example, to get a diurnal cycle but in a resolution
            of 15 minutes because hours (``resolution="h"``) are too coarse and
            minutes (``resolution="m"``) too fine you could do this:

            .. code-block:: python

                temporal_cycle(
                    x,               # the data
                    interval="D",    # aggregate to daily intervals
                    resolution="m",  # with a minutely resolution
                    # but before grouping, divide the minutes by 15
                    # and drop the precision to get quarterly resolution
                    modifier = lambda minutes: (minutes / 15).astype(int) * 15
                )

    Returns:
        groupby object : the aggregated data. Handle it like the return value
        of :meth:`pandas.DataFrame.groupby`, e.g. call ``mean()`` on it to
        calculate the average value for all periods.


    .. _numpy.datetime64:
        https://numpy.org/devdocs/reference/arrays.datetime.html
    """
    times, x = ParmesanAccessor.whats_time_whats_data(x, times=times)
    interval_dtype = np.dtype("datetime64[{}]".format(interval))
    resolution_dtype = np.dtype("datetime64[{}]".format(resolution))
    # converting times to a coarser type drops the resolution,
    # thus this gives us the interval starting points
    interval_starts = getattr(times, "values", times).astype(interval_dtype)
    # each time point is so much time into the interval
    time_into_interval = (
        getattr(times, "values", times).astype(resolution_dtype)
        - interval_starts
    )
    # turn the time difference into the resolution unit
    aggregate_axis = (
        time_into_interval / np.timedelta64(1, resolution)
    ).astype(int)
    return (x if hasattr(x, "groupby") else pd.Series(x, index=times)).groupby(
        modifier(aggregate_axis)
    )
