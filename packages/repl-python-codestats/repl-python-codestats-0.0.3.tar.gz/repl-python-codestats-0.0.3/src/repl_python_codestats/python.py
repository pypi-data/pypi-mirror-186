"""python
=========
"""
from typing import Callable

from repl_python_wakatime.python import install_hook as _install_hook

from . import codestats_hook


def install_hook(
    hook: Callable = codestats_hook, args: tuple = (), kwargs: dict = {}
) -> None:
    """Install hook.

    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict
    :rtype: None
    """
    _install_hook(hook, args, kwargs)
