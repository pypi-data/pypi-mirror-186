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

from . import _level_container
from typing import Union
import logging
import typing


class Palette:
    """The color palette used by `ColorFormatter`.
    
    """
    def __init__(self,
                 level_colors: _level_container.LevelContainer[Union[str, typing.Iterable[str]]]
                 ) -> None:
        """Note: all colors are defined as un-escaped ANSI codes with no ending, i.e. `x` in
        `\\033]xm`.


        """
        self._set_colors((logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
                          logging.CRITICAL), level_colors.iterall())
    
    def _set_colors(self, levels: typing.Iterable[int],
                    colors: typing.Generator[Union[str, typing.Iterable[str], None], None, None]
                    ) -> None:
        """Set `self.colors` given an iterable of logging levels and the generator returned from
        `LevelContainer.iterall()`.
        
        """
        entry = "\033[{}m"
        def format_many(values) -> str:
            try:
                return "".join(entry.format(v) for v in values)
            except Exception:
                raise ValueError("all colors provided in Palette.__init__ must be "
                                 "either a str or Iterable[str]")
        formatted_colors: dict[int, str] = {}
        for level, color in zip(levels, colors):
            if color is None:
                formatted_colors[level] = ""
                continue
            
            if isinstance(color, str):
                formatted_colors[level] = entry.format(color)
                continue
            
            formatted_colors[level] = format_many(color)

        self.colors = formatted_colors

    def enter(self, levelno: int) -> str:
        """Get the color formatting for a given level.
        
        """
        return self.colors.get(levelno, "")

    def exit(self, levelno: int) -> str:
        """Get the closing formatting for a given level (either `\\033[0m` or an empty str).
        
        """
        return "\033[0m" if self.colors.get(levelno, None) else ""


def parse_palettes(levelno: int, palettes: typing.Mapping[str, Palette]) -> dict[str, str]:
    """Parse all palettes into a dict of their corresponding `_c_enter` and `_c_exit` as keys and
    enter/exit values as values in preparation for formatting with the `Formatter`. Used in
    `plogging.Formatter.formatMessage`.
    
    """
    if not palettes:
        return {}
    itemview = palettes.items()
    c_enter_statements = {f"{n}{chr(2)}":p.enter(levelno) for n, p in itemview}
    c_exit_statements = {f"{n}{chr(3)}":p.exit(levelno) for n, p in itemview}
    return c_enter_statements | c_exit_statements
