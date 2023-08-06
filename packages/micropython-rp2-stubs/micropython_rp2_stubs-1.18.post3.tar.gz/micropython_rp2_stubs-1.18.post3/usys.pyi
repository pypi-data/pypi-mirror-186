"""
system specific functions. See: https://docs.micropython.org/en/v1.18/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
from typing import Dict, List, Tuple, Any

argv: list
byteorder: str

def exit(retval=0, /) -> Any:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

implementation: tuple
maxsize: int
modules: dict
path: list
platform: str

def print_exception(exc, file=stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).
    """
    ...

stderr: Any
stdin: Any
stdout: Any
version: str
version_info: tuple
