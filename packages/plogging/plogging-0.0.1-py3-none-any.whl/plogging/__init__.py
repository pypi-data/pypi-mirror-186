"""A formatter and set of utilities that bring pretty, highly-customizable and colored log messages
to the standard logging library.

:copyright: (c) 2023-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

__title__ = "plogging"
__author__ = "Tanner B. Corcoran"
__email__ = "tannerbcorcoran@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2023-present Tanner B. Corcoran"
__version__ = "0.0.1"
__description__ = ("A formatter and set of utilities that bring pretty, highly-customizable and "
                   "colored log messages to the standard logging library")
__url__ = "https://github.com/tanrbobanr/plogging"
__download_url__ = "https://pypi.org/project/plogging"


__all__ = (
    "Formatter",
    "LevelContainer",
    "Palette",
    "VALID_FLAGS",
    "COLOR_FORMAT_DEFAULTS",
    "setup_existing",
    "setup_new"
)


from ._formatter import Formatter
from ._level_container import LevelContainer
from ._palette import Palette
from .constants import (
    VALID_FLAGS,
    COLOR_FORMAT_DEFAULTS
)
from .utils import (
    setup_existing,
    setup_new
)
