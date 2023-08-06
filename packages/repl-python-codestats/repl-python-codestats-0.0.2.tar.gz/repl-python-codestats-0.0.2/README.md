# repl-python-codestats

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/repl-python-codestats/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/repl-python-codestats/main)
[![github/workflow](https://github.com/Freed-Wu/repl-python-codestats/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/repl-python-codestats/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/repl-python-codestats/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/repl-python-codestats)
[![readthedocs](https://shields.io/readthedocs/repl-python-codestats)](https://repl-python-codestats.readthedocs.io)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/repl-python-codestats/total)](https://github.com/Freed-Wu/repl-python-codestats/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/repl-python-codestats/latest/total)](https://github.com/Freed-Wu/repl-python-codestats/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)
[![github/v](https://shields.io/github/v/release/Freed-Wu/repl-python-codestats)](https://github.com/Freed-Wu/repl-python-codestats)

[![pypi/status](https://shields.io/pypi/status/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#description)
[![pypi/v](https://shields.io/pypi/v/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#history)
[![pypi/downloads](https://shields.io/pypi/dd/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#files)
[![pypi/format](https://shields.io/pypi/format/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/repl-python-codestats)](https://pypi.org/project/repl-python-codestats/#files)

A [codestats](https://codestats.net) plugin for python REPLs.

Supported REPLs:

- [x] [python](https://github.com/python/cpython):
  - executes
    [`str(sys.ps1)`](https://docs.python.org/3/library/sys.html#sys.ps1) after
    every input.
  - configure file:
    [`$PYTHON_STARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP).

```python
from repl_python_codestats.python import install_hook

install_hook()
```

- [x] [ptpython](https://github.com/prompt-toolkit/ptpython):
  - executes `get_ptpython().get_output_prompt()` after every output.
  - configure file: `.../ptpython/config.py`. `...` depends on OS.

```python
from ptpython.repl import PythonRepl
from repl_python_codestats.ptpython import install_hook


def configure(repl: PythonRepl) -> None:
    install_hook(repl)
```

- [x] [ipython](https://github.com/ipython/ipython):
  - executes
    `c.TerminalInteractiveShell.prompts_class(shell).out_prompt_tokens()` after
    every output.
  - configure file: `~/.ipython/profile_default/ipython_config.py`.

```python
from repl_python_codestats.iptpython import install_hook

install_hook(c)
```

- [x] [ptipython](https://github.com/prompt-toolkit/ptpython): Same as
  [ipython](https://github.com/ipython/ipython).
- [ ] [bpython](https://github.com/bpython/bpython)
- [ ] [xonsh](https://github.com/xonsh/xonsh)
- [ ] [mypython](https://github.com/asmeurer/mypython): Won't fix.
  - configure file: non-exist.

`install_hook()` must be after the customization of the prompt string and best
at the end of file.

## Configure

```python
install_hook(kwargs={"api_key": "your API key for codestats"})
```

Or see [keyring](docs/resources/requirements.md#keyring).

## Similar projects

- [wakatime plugins for python and many shells](https://wakatime.com/terminal)
- [codestats plugins](https://codestats.net/plugins)
