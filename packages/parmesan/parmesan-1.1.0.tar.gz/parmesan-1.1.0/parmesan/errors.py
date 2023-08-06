# system modules

# internal modules

# external modules


class ParmesanError(BaseException):
    """
    Base class for warnings raised by functions in the :mod:`parmesan` module.
    """


class OutOfBoundsError(ParmesanError):
    """
    Class for out-of-bounds errors
    """


class ParmesanWarning(UserWarning):
    """
    Base class for warnings raised by functions in the :mod:`parmesan` module.

    You can hide :class:`ParmesanWarning` s as usual in Python:

    .. code-block:: python

        import warnings
        warnings.filterwarnings(
            "ignore",
            category=parmesan.errors.ParmesanWarning
        )
    """


class OutOfBoundsWarning(ParmesanWarning):
    """
    Class for out-of-bounds warnings
    """
