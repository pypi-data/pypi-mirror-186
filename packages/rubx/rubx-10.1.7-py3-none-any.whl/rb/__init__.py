#!/bin/python

try:
    from .client import StartClient, UserMethods, __version__, __all__
except ImportError:
    from client import StartClient, UserMethods, __version__, __all__