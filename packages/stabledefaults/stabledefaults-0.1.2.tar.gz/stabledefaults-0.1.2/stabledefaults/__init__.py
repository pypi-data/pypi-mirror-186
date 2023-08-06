import importlib.metadata

from stabledefaults.decorator import stabledefaults

try:
    __version__ = importlib.metadata.version("stabledefaults")
except ModuleNotFoundError:
    __version__ = ""
