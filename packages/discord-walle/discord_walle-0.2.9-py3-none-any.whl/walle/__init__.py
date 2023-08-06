from pathlib import Path
from .core import *
from .configs import *
from .bot import *

try:
    version_path = Path(__file__).parent / "VERSION"
    version = version_path.read_text().strip()
except FileNotFoundError:
    version = "0.0.0"

__version__ = version
del version
