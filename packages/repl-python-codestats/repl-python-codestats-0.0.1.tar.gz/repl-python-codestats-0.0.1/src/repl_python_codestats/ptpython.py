"""ptpython
===========
"""
from typing import Callable

from ptpython.repl import PythonRepl
from repl_python_wakatime.ptpython import install_hook as _install_hook

from . import codestats_hook


def install_hook(
    repl: PythonRepl,
    hook: Callable = codestats_hook,
    args: tuple = (),
    kwargs: dict = {},
) -> PythonRepl:
    """Install hook.

    :param repl:
    :type repl: PythonRepl
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict
    :rtype: PythonRepl
    """
    return _install_hook(repl, hook, args, kwargs)
