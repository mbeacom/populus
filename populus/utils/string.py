import sys

from eth_utils import (
    to_bytes,
    to_text,
)


def normalize_class_name(value):
    """
    For `type()` calls:
    * Python 2 wants `str`
    * Python 3.4 wants `str`
    * Python 3.5 doesn't care.
    """
    if sys.version_info.major == 2:
        return to_bytes(value)
    return to_text(value)
