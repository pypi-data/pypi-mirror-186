# system modules
try:
    from parmesan.version import __version__
except ModuleNotFoundError:
    __version__ = "0.0.0"

# internal modules
import parmesan.bounds
import parmesan.units
import parmesan.processing
import parmesan.accessor
import parmesan.analysis
import parmesan.aggregate
import parmesan.gas
import parmesan.wind
import parmesan.stats
import parmesan.vector
import parmesan.radiation
import parmesan.clouds

# external modules
