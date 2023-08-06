"""An easy-to-use and highly customizable formatter used to turn a time value into a countdown
string.

:copyright: (c) 2023-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

__title__ = "countdownfmt"
__author__ = "Tanner B. Corcoran"
__email__ = "tannerbcorcoran@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2023-present Tanner B. Corcoran"
__version__ = "0.0.1"
__description__ = "An easy-to-use and highly customizable formatter used to turn a time value into a countdown string"
__url__ = "https://github.com/tanrbobanr/countdownfmt"
__download_url__ = "https://pypi.org/project/countdownfmt"

__all__ = (
    "Countdown",
    "constants"
)

from ._countdown import Formatter as Countdown
from . import constants
