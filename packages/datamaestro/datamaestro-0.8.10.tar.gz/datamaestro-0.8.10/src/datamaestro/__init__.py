# flake8: noqa: F401 (re-exports)
from .context import (
    Context,
    Repository,
    get_dataset,
    prepare_dataset,
)

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = None
