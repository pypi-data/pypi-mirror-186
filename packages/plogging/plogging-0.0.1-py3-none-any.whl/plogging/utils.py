"""MIT License

Copyright (c) 2023-present Tanner B. Corcoran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from . import _formatter
from . import _palette
from . import _level_container
from . import types
import logging
import sys
import os
import io


def _stream_supports_color(stream: io.TextIOBase) -> bool:
    """Return whether or not the running system's terminal supports ANSI color formatting.
    
    """

    def vt_codes_enabled_in_windows_registry() -> bool:
        try:
            import winreg
        except ImportError:
            return False
        else:
            try:
                reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Console")
                reg_key_value, _ = winreg.QueryValueEx(reg_key, "VirtualTerminalLevel")
            except FileNotFoundError:
                return False
            else:
                return reg_key_value == 1

    is_a_tty = hasattr(stream, "isatty") and stream.isatty()

    if sys.platform != "win32":
        return is_a_tty

    return is_a_tty and (
        "ANSICON" in os.environ
        or "PYCHARM_HOSTED" in os.environ # pycharm
        or "WT_SESSION" in os.environ # Windows terminal
        or os.environ.get("TERM_PROGRAM") == "vscode" # vscode
        or vt_codes_enabled_in_windows_registry()
    )


def default_formatter() -> _formatter.Formatter:
    """Create the default `Formatter` instance.
    
    """
    return _formatter.Formatter(
        _level_container.LevelContainer(
            default="{asctime} {levelname:<8} {name} {message}"
        ),
        "%Y-%m-%d %H:%M:%S",
        backup_fmts=_level_container.LevelContainer(
            default="[{asctime}] [{levelname:<8}] {name}: {message}"
        ),
        asctime=_palette.Palette(
            _level_container.LevelContainer(
                default="30;1"
            )
        ),
        levelname=_palette.Palette(
            _level_container.LevelContainer(
                "32;1",
                "34;1",
                "33;1",
                "31;1",
                "41"
            )
        ),
        name=_palette.Palette(
            _level_container.LevelContainer(
                default="35"
            )
        ),
        exc_text=_palette.Palette(
            _level_container.LevelContainer(
                default="31"
            )
        )
    )


def setup_existing(logger: logging.Logger, *, level: types.LoggingLevel = None,
                   handler: logging.Handler = None, formatter: logging.Formatter = None) -> None:
    """Setup formatting and handling on an existing `Logger`.

    Arguments
    ---------
    level : LoggingLevel
        If defined, the logging level for `logger` will be set to `level`.
    handler : Handler
        If defined, the handler for `logger` will be set to `handler`. If not defined, a new
        `StreamHandler` will be used.
    formatter : Formatter
        If defined, the formatter for `handler` will be set to `formatter`. If not defined, a
        default instance of `plogging.Formatter` will be used instead.
    
    Notes
    -----
    If `formatter` is an instance of `plogging.Formatter`, the `stream_supports_color` attribute on
    the formatter will be set to `True` if the handler stream supports color, otherwise `False`. If
    this value is already set, then it will not be changed.
    
    """
    handler = handler or logging.StreamHandler()

    if formatter is None:
        formatter = default_formatter()
    
    if isinstance(formatter, _formatter.Formatter) and formatter.stream_supports_color is None:
        if not hasattr(handler, "stream"):
            stream_supports_color = False
        else:
            stream_supports_color = _stream_supports_color(getattr(handler, "stream"))
        formatter.stream_supports_color = stream_supports_color

    if level:
        logger.setLevel(level)

    handler.setFormatter(formatter)
    logger.addHandler(handler)


def setup_new(name: str, *, level: types.LoggingLevel = None, package: str = None,
              handler: logging.Handler = None,
              formatter: logging.Formatter = None) -> logging.Logger:
    """Setup a new `Logger` with the given `name` and optional `package` (will be concatenated into
    `{package}.{name}). `level`, `handler`, and `formatter` are the same as those found in
    `setup_existing`.
    
    """
    if package:
        _name = f"{package}.{name}"
    else:
        _name = name
    logger = logging.getLogger(_name)
    setup_existing(logger, level=level, handler=handler, formatter=formatter)
    return logger
