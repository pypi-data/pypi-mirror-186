"""Configuration and error templates."""

import inspect
from pathlib import Path
from pprint import pformat

from web.framework.util import tx
from web.slrzd import highlight

__all__ = ["inspect", "pformat", "highlight", "tx", "getsourcelines", "Path"]


def getsourcelines(obj):
    """Return number of lines of source used to implement obj."""
    try:
        return inspect.getsourcelines(obj)
    except IOError:
        return "", 0
