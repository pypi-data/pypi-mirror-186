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

from typing import Union
from . import types
import string
str_formatter = string.Formatter()
del string


class FormatContainer:
    def __init__(self, conversion: str, format_spec: str, field_name: str = None,
                 field_name_append: str = None) -> None:
        self.conversion = conversion
        self.format_spec = format_spec
        self.field_name = field_name
        self.field_name_append = field_name_append
    
    def __str__(self) -> str:
        return f"{{{self.field_name}{self.field_name_append}{self.conversion}{self.format_spec}}}"


class FormatStringConverter:
    def __init__(self) -> None:
        self.values: list[Union[str, FormatContainer]] = []
        self.awaiting_exit: FormatContainer = None

    @staticmethod
    def _conversion(conversion: Union[str, None]) -> str:
        return f"!{conversion}" if conversion else ""

    @staticmethod
    def _format_spec(format_spec: Union[str, None]) -> str:
        return f":{format_spec}" if format_spec else ""

    @staticmethod
    def _format_statement(field_name: Union[str, None], conversion: str, format_spec: str) -> str:
        return f"{{{field_name or ''}{conversion}{format_spec}}}"

    def _add_flag(self, field_name: Union[str, None], conversion: str, format_spec: str) -> None:
        self.values.append(FormatStringConverter._format_statement(field_name, conversion,
                                                                   format_spec))

    def _enter(self, conversion: str, format_spec: str) -> None:
        if self.awaiting_exit:
            raise ValueError("new enter flag found before previous enter flag was closed")
        enter = FormatContainer(conversion, format_spec, field_name_append=chr(2))
        self.values.append(enter)
        self.awaiting_exit = enter
    
    def _exit(self, conversion: str, format_spec: str) -> None:
        if not self.awaiting_exit:
            raise ValueError("exit flag used before enter flag")
        if self.awaiting_exit.field_name is None:
            raise ValueError("exit flag used without a contained flag; make sure you have at least"
                             " one flag between your enter and exit flags")
        self._add_flag(f"{self.awaiting_exit.field_name}{chr(3)}", conversion, format_spec)
        self.awaiting_exit = None
    
    def _stringify_values(self) -> list[str]:
        return [str(v) for v in self.values]

    def to_color_format(self, fmt: types.SupportsBracketFormat) -> str:
        for literal_text, field_name, format_spec, conversion in str_formatter.parse(fmt):
            if literal_text:
                self.values.append(literal_text)
            
            _conversion = self._conversion(conversion)
            _format_spec = self._format_spec(format_spec)

            if field_name is None and format_spec is None and conversion is None:
                continue

            if not field_name:
                self._add_flag(None, _conversion, _format_spec)
                continue
            
            if field_name.startswith("_"):
                self._add_flag(field_name[1:], _conversion, _format_spec)
                continue

            if field_name == "enter":
                self._enter(_conversion, _format_spec)
                continue
            
            if field_name == "exit":
                self._exit(_conversion, _format_spec)
                continue
            
            if self.awaiting_exit and self.awaiting_exit.field_name is not None:
                self._add_flag(field_name, _conversion, _format_spec)
                continue
            
            if self.awaiting_exit:
                self.awaiting_exit.field_name = field_name
                self._add_flag(field_name, _conversion, _format_spec)
                continue
            
            self._add_flag(f"{field_name}{chr(2)}", "", "")
            self._add_flag(field_name, _conversion, _format_spec)
            self._add_flag(f"{field_name}{chr(3)}", "", "")

        values = self._stringify_values()

        self.values = []
        self.awaiting_exit = None
        
        return "".join(values)
    
    @staticmethod
    def strip_color(fmt: types.SupportsBracketFormat) -> str:
        updated: list[str] = []

        for literal_text, field_name, format_spec, conversion in str_formatter.parse(fmt):
            if literal_text:
                updated.append(literal_text)
            
            _conversion = FormatStringConverter._conversion(conversion)
            _format_spec = FormatStringConverter._format_spec(format_spec)

            if field_name in ["enter", "exit"]:
                continue
            
            if field_name and field_name[-1] in [chr(2), chr(3)]:
                continue
            
            if field_name and field_name.startswith("_"):
                field_name = field_name[1:]

            updated.append(FormatStringConverter._format_statement(field_name, _conversion,
                                                                   _format_spec))
        
        return "".join(updated)
