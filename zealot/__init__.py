import sys

from .exceptions import TooOldPythonException

if sys.version_info <= (3, 6):
    raise TooOldPythonException('You need to use python 3.6 at least')
