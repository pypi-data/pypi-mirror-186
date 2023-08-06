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
import typing

_valid_levels = (10, 20, 30, 40, 50)
_name_to_level = {
    "CRITICAL": 50,
    "FATAL": 50,
    "ERROR": 40,
    "WARN": 30,
    "WARNING": 30,
    "INFO": 20,
    "DEBUG": 10,
}


def _verify_level(level: types.LoggingLevel) -> int:
    if isinstance(level, int) and not isinstance(level, bool):
        if level not in _valid_levels:
            raise ValueError(f"Unknown level: {level}")
        return level
    
    if isinstance(level, str):
        if level not in _name_to_level:
            raise ValueError(f"Unknown level: {level}")
        return _name_to_level[level]
    
    raise TypeError(f"Invalid type for level: {type(level).__name__}")


class LevelContainer(typing.Generic[types.T]):
    """A container to hold and obtain values for each of the logging levels available in Python's
    standard `logging` library.
    
    """
    def __init__(self, debug: typing.Optional[types.T] = None,
                 info: typing.Optional[types.T] = None,
                 warning: typing.Optional[types.T] = None,
                 error: typing.Optional[types.T] = None,
                 critical: typing.Optional[types.T] = None, *,
                 default: typing.Optional[types.T] = None) -> None:
        """Values may be provided for each of the logging levels as well as a default fallback for
        any levels whose values are set to or remain `None`.
        
        """
        self._debug = debug
        self._info = info
        self._warning = warning
        self._error = error
        self._critical = critical
        self._default = default
        self._levelmap = {
            10: self.debug,
            20: self.info,
            30: self.warning,
            40: self.error,
            50: self.critical
        }
    
    def _get(self, value: typing.Optional[types.T],
             default: Union[types.VT, types.MISSING]) -> typing.Optional[Union[types.T, types.VT]]:
        """Return value or `_default` or `default` or None.
        
        """
        return value or self._default or (default if default is not types.MISSING else None)

    @typing.overload
    def debug(self) -> typing.Optional[types.T]: ...
    @typing.overload
    def debug(self, default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def debug(self, default: types.VT = types.MISSING,
              /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the `DEBUG` logging level, with an optional default if both the value
        and container default are undefined.
        
        """
        return self._get(self._debug, default)

    @typing.overload
    def info(self) -> typing.Optional[types.T]: ...
    @typing.overload
    def info(self, default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def info(self, default: types.VT = types.MISSING,
             /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the `INFO` logging level, with an optional default if both the value
        and container default are undefined.
        
        """
        return self._get(self._info, default)

    @typing.overload
    def warning(self) -> typing.Optional[types.T]: ...
    @typing.overload
    def warning(self, default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def warning(self, default: types.VT = types.MISSING,
                /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the `WARNING` logging level, with an optional default if both the value
        and container default are undefined.
        
        """
        return self._get(self._warning, default)

    @typing.overload
    def error(self) -> typing.Optional[types.T]: ...
    @typing.overload
    def error(self, default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def error(self, default: types.VT = types.MISSING,
              /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the `ERROR` logging level, with an optional default if both the value
        and container default are undefined.
        
        """
        return self._get(self._error, default)

    @typing.overload
    def critical(self) -> typing.Optional[types.T]: ...
    @typing.overload
    def critical(self, default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def critical(self, default: types.VT = types.MISSING,
                 /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the `CRITICAL` logging level, with an optional default if both the
        value and container default are undefined.
        
        """
        return self._get(self._critical, default)
    
    @typing.overload
    def get(self, level: types.LoggingLevel, /) -> typing.Optional[types.T]: ...
    @typing.overload
    def get(self, level: types.LoggingLevel,
            default: types.VT, /) -> typing.Optional[Union[types.T, types.VT]]: ...
    def get(self, level: types.LoggingLevel,
            default: types.VT = types.MISSING, /) -> typing.Optional[Union[types.T, types.VT]]:
        """Get the value for the the given logging level, with an optional default if both the
        value and container default are undefined.
        
        """
        return self._levelmap[_verify_level(level)](default)

    @typing.overload
    def iterall(self) -> typing.Generator[typing.Optional[types.T], None, None]: ...
    @typing.overload
    def iterall(self, debug_default: types.VT = types.MISSING,
                info_default: types.VT = types.MISSING, warning_default: types.VT = types.MISSING,
                error_default: types.VT = types.MISSING, critical_default: types.VT = types.MISSING
                ) -> typing.Generator[typing.Optional[Union[types.T, types.VT]], None, None]: ...
    def iterall(self, debug_default: types.VT = types.MISSING,
                info_default: types.VT = types.MISSING, warning_default: types.VT = types.MISSING,
                error_default: types.VT = types.MISSING, critical_default: types.VT = types.MISSING
                ) -> typing.Generator[typing.Optional[Union[types.T, types.VT]], None, None]:
        """Iterate through all logging levels, with optional defaults for each level.
        
        """
        funcs = (self.debug, self.info, self.warning, self.error, self.critical)
        defaults = (debug_default, info_default, warning_default, error_default, critical_default)
        for f, d in zip(funcs, defaults):
            yield f(d)
