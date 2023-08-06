from .plugin import JunitPlugin

__all__ = [

    "__version__",

    "__version_tuple__",

    "JunitPlugin",

]

try:
    from ._version import __version__, __version_tuple__
except ImportError:
    __version__ = ""
    __version_tuple__ = tuple()
