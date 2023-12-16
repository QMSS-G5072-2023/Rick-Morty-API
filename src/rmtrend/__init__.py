# read version from installed package
from importlib.metadata import version
__version__ = version("rmtrend")

from rmtrend import fetch_character_info
from rmtrend import fetch_location_info
from rmtrend import recent_reddit
