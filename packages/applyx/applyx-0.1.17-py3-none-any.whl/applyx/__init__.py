# coding=utf-8

import sys
if (sys.version_info.major, sys.version_info.minor) >= (3, 10):
    # patch for attrdict
    import collections
    from collections.abc import Mapping, MutableMapping, Sequence
    collections.Mapping = Mapping
    collections.MutableMapping = MutableMapping
    collections.Sequence = Sequence


from applyx._version import VERSION
__version__ = VERSION

__all__ = [
    "__version__",
    "VERSION"
]
