try:
    from fime._version import __version__, __version_tuple__
except ImportError:
    __version__ = version = '0+devfallback'
    __version_tuple__ = version_tuple = (0, 'devfallback')
