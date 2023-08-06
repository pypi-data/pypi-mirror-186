# system modules
import itertools
import math
import warnings

# internal modules
from parmesan.errors import ParmesanWarning
from parmesan.accessor import ParmesanAccessor

# external modules
import numpy as np
import pandas as pd
import scipy.interpolate
import scipy.signal
import scipy.fftpack
import scipy.optimize


def power_spectrum(
    x,
    y,
    window="hann",
    blocks=1,
    overlap=True,
    detrend="linear",
    norm=True,
    interpolation=None,
    returnvalue=("frequency", "power"),
):
    """
    Calculate a power spectrum for a one-dimensional signal of real values

    This is the workhorse for the :func:`spectrum` convenience wrapper which
    should be preferred over direct invocation of this function.

    Args:
        x (sequence of floats): the x coordinate (e.g. time in seconds)
        y (sequence of floats): the signal
        window (str, optional): windowing function. See
            :any:`scipy.signal.get_window`.
        blocks (int, optional): How many overlapping blocks to use. Defaults to
            1.
        overlap (bool, optional): whether to let the blocks overlap by 50% of
            their width. This means, only an odd number of blocks can be used
            if ``overlap=True``. A warning is raised and the block size
            increased automatically otherwise.
        interpolation (str, optional): interpolation method to use for
            unevenly-spaced times. See ``kind`` argument of
            :func:`scipy.interpolate.interp1d`. By default, no
            interpolation is performed and a warning is raised for
            unevenly-space times.
        detrend (str, optional): detrending method. See
            :any:`scipy.signal.detrend`.
        norm (bool, optional): whether to divide the signal by its length
        returnvalue (sequence of str, optional): What to return. Values:

            ``"frequency"``
                the frequencies in Hz

            ``"power"``
                the spectral power

            ``"blocks"``
                the (possibly conditioned) timeseries blocks used to calculate
                the spectrum

            ``"kolmogorov"``
                a power-law fit ``A * frequency ^ (-5/3)``

            ``"kolmogorov-scale"``
                factor A of a power-law fit ``A * frequency ^ (-5/3)``

    Returns:
        sequence : as specified with ``returnvalue``
    """
    # convert inputs to numpy arrays
    x, y = map(np.asarray, (x, y))
    # make sure number of blocks is correct
    if overlap and blocks % 2 == 0:
        blocks += 1
        warnings.warn(
            "An odd number of blocks is needed if overlap=True. "
            "Increasing number of blocks to {}.".format(blocks),
            category=ParmesanWarning,
        )
    # drop older values to fit the number of blocks
    n_base_blocks = math.ceil(blocks / 2) if overlap else blocks
    if x.size > n_base_blocks:
        drop = x.size % n_base_blocks
        if drop:
            warnings.warn(
                "Dropping first {} of {} samples to fit "
                "evenly into {} blocks".format(drop, x.size, n_base_blocks),
                category=ParmesanWarning,
            )
            x, y = x[drop:], y[drop:]
    block_size = int(x.size / n_base_blocks)
    timesteps = np.unique(np.diff(x))
    # TODO: rounding issues might give false negatives here
    evenly_spaced = timesteps.size == 1 or (
        (np.median(np.diff(timesteps)) / np.median(timesteps)) < 1e-1
    )
    # interpolate to evenly-spaced times if necessary
    if not evenly_spaced:
        if x.size > 1:
            if interpolation:
                interpolator = scipy.interpolate.interp1d(x, y)
                x = np.linspace(x.min(), x.max(), num=x.size)
                y = interpolator(x)
            else:
                warnings.warn(
                    "FFT over unevenly-spaced x coordinates "
                    "({} occurring timesteps: {}) will "
                    "yield unexpected results! "
                    "Consider setting interpolation='linear' "
                    "for example.".format(
                        timesteps.size,
                        timesteps,
                    ),
                    category=ParmesanWarning,
                )
    # split into blocks
    y_blocks = []
    if overlap and blocks > 1:
        y_blocks.extend(np.split(y, n_base_blocks))
        n_overlap_blocks = blocks - n_base_blocks
        overlap_block_region = slice(
            math.floor(block_size / 2), -math.ceil(block_size / 2)
        )
        assert len(y[overlap_block_region]) % block_size == 0, (
            "Overlap block region should be divisible by {}, "
            "but has size {}"
        ).format(block_size, len(y[overlap_block_region]))
        y_blocks.extend(
            np.split(
                y[overlap_block_region],
                n_overlap_blocks,
            )
        )
    else:
        y_blocks.extend(np.split(y, blocks))
    # detrend
    if detrend:
        y_blocks = tuple(
            scipy.signal.detrend(block, type=detrend) for block in y_blocks
        )
    # apply a window to all blocks if wanted
    if window:
        if window.lower() == "hanning":
            warnings.warn(
                "scipy v1.9 removed the 'hanning' alias for 'hann'. "
                "Please change your usage of "
                "window='hanning' to window='hann'.",
                DeprecationWarning,
            )
            window = "hann"
        y_blocks = tuple(
            block * scipy.signal.get_window(window, block.size)
            for block in y_blocks
        )
    # calculate power spectrum
    power = (
        # calculate the absolute value of fourrier values
        np.abs(
            # calculate average across blocks/columns
            np.mean(
                # stack fft block resuls as rows on top of each other
                np.vstack(
                    tuple(
                        # Fourrier transform each block
                        map(
                            scipy.fft.rfft,
                            # norm the blocks with the sample size if wanted
                            (
                                [block / block.size for block in y_blocks]
                                if norm
                                else y_blocks
                            ),
                        )
                    )
                ),
                axis=0,
            )
        )
        # square the absolute value to get the power
        ** 2
    )
    # calculate frequencies
    tdiff = np.median(np.unique(np.diff(x)))
    freq = scipy.fft.rfftfreq(block_size, tdiff or 1)
    retvals = dict(
        frequency=freq,
        power=power,
        blocks=y_blocks,
    )
    if "kolmogorov" in returnvalue:

        def powerlaw(f, scale):
            return scale * f ** (-5 / 3)

        (scale,), pcov = scipy.optimize.curve_fit(
            powerlaw, freq[1:], power[1:]
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            retvals["kolmogorov"] = powerlaw(freq, scale)
        retvals["kolmogorov-scale"] = scale
    return tuple(retvals.get(k, None) for k in returnvalue)


@ParmesanAccessor.register
def spectrum(x, times=None, with_kolmogorov=False, **kwargs):
    """
    Calculate a power spectrum of a one-dimensional timeseries of real values

    This is a convenience wrapper for :func:`power_spectrum`.

    For an example, see the `Spectrum Example`_.

    .. _Spectrum Example: ../notebooks/spectrum.ipynb

    Args:
        x (pandas.DataFrame or pandas.Series or numpy.ndarray): the values
            to calculate the spectrum for
        times (array-like of datetime-like, optional): the times to use
        with_kolmogorov (bool, optional): add a power law fit to the output
        **kwargs: further keyword arguments to :func:`power_spectrum`

    Returns:
        sequence, :class:`pandas.Series` or :class:`pandas.DataFrame` :

        Depending on the type of ``x``:

        :class:`numpy.ndarray`
            the sequence ``frequencies,power`` of :class:`numpy.ndarray` s

        :class:`pandas.Series`
            a new :class:`pandas.Series` of the power with the frequency as
            index

        :class:`pandas.DataFrame`
            a new :class:`pandas.DataFrame` with the frequency as index and
            corresponding columns containing the power

    """
    times, x = ParmesanAccessor.whats_time_whats_data(x, times=times)
    # calculate time in seconds
    t = (times - times.min()) / np.timedelta64(1, "s")
    if (returnvalue := kwargs.get("returnvalue")) and returnvalue != (
        v := ("frequency", "power")
    ):
        warnings.warn(
            f"Overwriting {returnvalue = !r} with {v!r}. "
            f"Use power_spectrum(..., {returnvalue = !r}) directly"
            f"If you really need this",
            category=ParmesanWarning,
        )
        kwargs["returnvalue"] = v
        del v
    if isinstance(x, pd.Series):
        if with_kolmogorov:
            freq, power, kolmogorov, kolmogorov_scale = power_spectrum(
                x=t,
                y=x,
                **{
                    **kwargs,
                    **dict(
                        returnvalue=(
                            "frequency",
                            "power",
                            "kolmogorov",
                            "kolmogorov-scale",
                        )
                    ),
                },
            )
            return pd.DataFrame(
                {
                    x.name: power,
                    f"{x.name} power-law "
                    f"[{kolmogorov_scale:g} f ^ (-5/3)]": kolmogorov,
                },
                index=pd.Index(freq, name="frequency [Hz]"),
            )
        else:
            freq, power = power_spectrum(x=t, y=x, **kwargs)
            s = pd.Series(power, name=x.name)
            s.index = pd.Index(freq, name="frequency [Hz]")
            return s
    elif isinstance(x, pd.DataFrame):
        if with_kolmogorov:
            warnings.warn(
                f"Currently, {with_kolmogorov = } "
                f"is not implemented for DataFrame inputs. "
                f"But you can select a specific column like "
                f"df[{next(iter(x.columns),'colname')!r}]"
                f".parmesan.spectrum({with_kolmogorov = !r})",
                category=ParmesanWarning,
            )
        spectra = {c: power_spectrum(x=t, y=x[c], **kwargs) for c in x}
        return pd.DataFrame(
            {c: power for c, (freq, power) in spectra.items()},
            index=pd.Index(
                next(freq for c, (freq, power) in spectra.items()),
                name="frequency [Hz]",
            ),
        )
    else:
        return power_spectrum(x=t, y=x, **kwargs)


def structure_function(x, y, order=2, normed=True):

    """
    Calculate the structure function for a one-dimensional signal of real
    values

    This is the workhorse for the :func:`structure` convenience wrapper which
    should be preferred over direct invocation of this function.

    Args:
        x (sequence of floats): the x coordinate (e.g. time in seconds)
        y (sequence of floats): the signal
        order (int, optional): The order of the structure function
        normed (bool, optional): whether to norm the structure function with
            the variance of the signal.

    Returns:
        sequence : time shift, structure function as arrays
    """

    # convert inputs to numpy arrays
    t = np.asarray(x)
    y = np.asarray(y)

    # Frequency calculation
    tstep = np.roll(t, -1) - t
    f_vec = 1 / tstep[: (len(t) - 1)]
    freq = np.nanmean(f_vec)

    if np.std(f_vec > 0.01 * freq):
        raise ValueError(
            "It seems that the timeserie is not equally spaced. "
            "Plese use a resampled DataFrame or make sure to have constant "
            "sampling rate"
        )

    # Algorithm for the structure function ###################################
    n = len(y)
    tau_max = int(n / 4)
    D = np.zeros(tau_max)

    for i in range(tau_max):
        delta = []
        full_delta = (y - np.roll(y, -(i))) ** order
        D[i] = np.nanmean(abs(full_delta[: (n - (i + 1))]))

    shift = np.linspace(0, tau_max, tau_max) / freq

    return (shift, (D / (2 * np.var(y)) if normed else D))


@ParmesanAccessor.register
def structure(x, times=None, **kwargs):
    """
    Calculate the structure function of a one-dimensional timeseries of real
    values

    This is a convenience wrapper for :func:`structure_function`.

    Args:
        x (pandas.DataFrame or pandas.Series or numpy.ndarray): the values
            to calculate the structure function for
        times (array-like of datetime-like, optional): the times to use
        **kwargs: further keyword arguments to :func:`structure_function`

    Returns:
        sequence, :class:`pandas.Series` or :class:`pandas.DataFrame` :

        Depending on the type of ``x``:

        :class:`numpy.ndarray`
            the sequence ``timeshifts,structurefunction`` of
            :class:`numpy.ndarray` s

        :class:`pandas.Series`
            a new :class:`pandas.Series` of the structure function with the
            timeshift as index

        :class:`pandas.DataFrame`
            a new :class:`pandas.DataFrame` with the timeshift as index and
            corresponding columns containing the structurefunction

    """
    times, x = ParmesanAccessor.whats_time_whats_data(x, times=times)
    # calculate time in seconds
    t = (times - times.min()) / np.timedelta64(1, "s")
    if isinstance(x, pd.Series):
        shift, DD = structure_function(x=t, y=x, **kwargs)
        s = pd.Series(DD, name=x.name)
        s.index = pd.Index(shift, name="Time Shift [s]")
        return s
    elif isinstance(x, pd.DataFrame):
        structures = {c: structure_function(x=t, y=x[c], **kwargs) for c in x}
        df = pd.DataFrame(
            {c: DD for c, (shift, DD) in structures.items()},
        )
        df.index = pd.Index(
            next(shift for c, (shift, DD) in structures.items()),
            name="Time Shift [s]",
        )
        return df
    else:
        return structure_function(x=t, y=x, **kwargs)
