"""ipython
==========
"""
from typing import Callable

from repl_python_wakatime.ipython import install_hook as _install_hook
from traitlets.config.loader import Config

from . import codestats_hook


def install_hook(
    c: Config,
    hook: Callable = codestats_hook,
    args: tuple = (),
    kwargs: dict = {},
) -> Config:
    """Install hook.

    :param c:
    :type c: Config
    :param hook:
    :type hook: Callable
    :param args:
    :type args: tuple
    :param kwargs:
    :type kwargs: dict
    :rtype: Config
    """
    return _install_hook(c, hook, args, kwargs)
