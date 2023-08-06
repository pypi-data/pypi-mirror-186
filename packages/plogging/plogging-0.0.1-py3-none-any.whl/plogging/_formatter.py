"""The core module which defines `Formatter`.

:copyright: (c) 2023-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

__author__ = "Tanner B. Corcoran"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2023-present Tanner B. Corcoran"

from . import _level_container
from . import _converter
from . import constants
from . import _palette
from . import types
import traceback
import logging
import string
import typing
import io
import re

fmt_spec = re.compile(r"^(.?[<>=^])?[+ -]?#?0?(\d+|{\w+})?[,_]?(\.(\d+|{\w+}))?[bcdefgnosx%]?$",
                      re.IGNORECASE)
field_spec = re.compile(r"^(\d+|\w+)(\.\w+|\[[^]]+\])*$")
str_formatter = string.Formatter()


def _validate_fmt(fmt: str, extra_keys: list[str]) -> None:
    """Validate the input format, ensure it is the correct string formatting style.
    
    """
    fields: set[str] = set()
    try:
        for literal_text, field_name, format_spec, conversion in str_formatter.parse(fmt):
            if field_name:
                if not field_spec.match(field_name):
                    raise ValueError(f"invalid field name/expression: {field_name}")
                fields.add(field_name)
            if conversion and conversion not in 'rsa':
                raise ValueError(f"invalid conversion: {conversion}")
            if format_spec and not fmt_spec.match(format_spec):
                raise ValueError(f"bad specifier: {format_spec}")
    except ValueError as exc:
        raise ValueError(f"Invalid format: {exc}")
    if not fields:
        raise ValueError("Invalid format: no fields")
    fields = {f[1:] if f.startswith("_") else f for f in fields}
    missing = fields - set(constants.VALID_FLAGS + list(extra_keys))
    if missing:
        raise ValueError(f"Missing defaults: {', '.join(missing)}")


def _format_defaults(default_keys: list[str]) -> dict:
    if not default_keys:
        return {}
    c_enter_statements = {f"{name}{chr(2)}":"" for name in default_keys}
    c_exit_statements = {f"{name}{chr(3)}":"" for name in default_keys}
    return c_enter_statements | c_exit_statements


class Formatter(logging.Formatter):
    """A `logging.Formatter` subclass equipped to handle both standard and color formatting.
    
    """
    def __init__(self, fmts: _level_container.LevelContainer[types.SupportsBracketFormat],
                 datefmt: str = None, defaults: typing.Mapping = None,
                 force_ansi: bool = False,
                 backup_fmts: _level_container.LevelContainer[types.SupportsBracketFormat] = None,
                 **palettes: _palette.Palette) -> None:
        """
        Arguments
        ---------
        fmts : LevelContainer[SupportsBracketFormat]
            The container specifying format strings for each (or all) of the logging levels. Unlike
            `logging.Formatter`, which can use bracket, percent, and shell formatting, this
            formatter requires the user to use bracket formatting. The list of allowed flags can be
            acquired through the `VALID_FLAGS` module variable.
        datefmt : str, default=None
            The date format string used when formatting the `asctime` flag. This uses the same
            formatting style as `datetime`'s `strftime` and `strptime` methods.
        defaults : Mapping, default=None
            Default values for any flag.
        force_ansi : bool, default=False
            If `True`, the ANSI color coding will be included in the output regardless of whether or
            not the terminal in use supports color.
        backup_fmts : LevelContainer[SupportsBracketFormat], default=None
            The formats used when the current terminal use does not support color. If `None`, the
            main formats will be used (though without colors applied).
        **palettes : Palette
            Additional keyword-only arguments used to set the colors of various flags for different
            logging levels. All keys must be valid flags; a list of which can be acquired through
            the `VALID_FLAGS` module variable.
        
        Notes
        -----
        The `stream_supports_color` attribute must be set to a boolean value post-instantiation.
        This variable indicates whether or not the current stream supports ANSI color formatting.
        When using `setup_existing` or `setup_new`, this is set automatically.

        """
        self.defaults = defaults or {}
        self.default_keys = list(self.defaults.keys())
        self._ensure_sufficient_formats(fmts)
        self._ensure_format_validity(fmts, self.default_keys)
        if backup_fmts:
            self._ensure_format_validity(backup_fmts, self.default_keys)
            self._fix_backups(fmts, backup_fmts, False)
        else:
            backup_fmts = _level_container.LevelContainer()
            self._fix_backups(fmts, backup_fmts, True)
        self._update_formats(fmts)
        

        self.force_ansi = force_ansi
        self.stream_supports_color = None
        self.palettes = palettes
        self.fmts = fmts
        self.backup_fmts = backup_fmts
        
        super().__init__()
    
    @staticmethod
    def _ensure_format_validity(fmt: _level_container.LevelContainer[types.SupportsBracketFormat],
                                extras: "list[str]") -> None:
        """Ensure all formats in `fmt` are valid bracket-style format strings and that all fields
        are in either VALID_FLAGS or `extras`.
        
        """
        for fmt_str in fmt.iterall():
            if fmt_str is not None:
                _validate_fmt(fmt_str, extras)

    @staticmethod
    def _ensure_sufficient_formats(fmt: _level_container.LevelContainer[types.SupportsBracketFormat]
                                   ) -> None:
        """Ensure that all logging levels are covered in `fmt`.
        
        """
        # this case would technically be covered in `.iterall()`, but this is faster
        if fmt._default is not None:
            return

        if not all(x is not None for x in fmt.iterall()):
            raise ValueError("all levels in fmt must have a format string (either set the default "
                             "or provide a value for each level)")

    @staticmethod
    def _update_formats(fmt: _level_container.LevelContainer[types.SupportsBracketFormat]) -> None:
        """Update each format string in `fmt` to a color-ready format string.
        
        """
        converter = _converter.FormatStringConverter()
        for attr in ("_debug", "_info", "_warning", "_error", "_critical", "_default"):
            _fmt: str = getattr(fmt, attr)
            if _fmt is not None:
                setattr(fmt, attr, converter.to_color_format(_fmt))
    
    @staticmethod
    def _fix_backups(fmts: _level_container.LevelContainer[types.SupportsBracketFormat],
                     backup_fmts: _level_container.LevelContainer[types.SupportsBracketFormat],
                     make_new: bool) -> None:
        if make_new:
            for attr in ("_debug", "_info", "_warning", "_error", "_critical", "_default"):
                val = getattr(fmts, attr)
                if val:
                    setattr(backup_fmts, attr, _converter.FormatStringConverter.strip_color(val))
            return
        
        for attr in ("debug", "info", "warning", "error", "critical"):
            val = getattr(backup_fmts, attr)()
            if not val:
                setattr(backup_fmts, f"_{attr}", getattr(fmts, attr)()) 

    def _ensure_ssc_set(self) -> None:
        """Ensure that `stream_supports_color` is set to a boolean value.
        
        """
        if self.stream_supports_color not in [True, False, 1, 0]:
            raise ValueError("ColorFormatter.stream_supports_color must be a boolean")

    def _get_fmt_str(self, levelno: int) -> str:
        """Get the format string from `fmts` or `backup_fmts` given the leveno.
        
        """
        self._ensure_ssc_set()
        
        if self.force_ansi is True or self.stream_supports_color is True:
            return self.fmts.get(levelno)
        
        if self.stream_supports_color is False and self.backup_fmts is None:
            # no colors applied
            return self.fmts.get(levelno)
        
        # if we have a backup format and the stream does not support color
        return self.backup_fmts.get(levelno) or self.fmts.get(levelno)
    
    def _get_fmt_kwargs(self, record: logging.LogRecord) -> dict:
        """Get the kwargs from `fmts` or `backup_fmts` for formatting the format string given the
        `LogRecord`.
        
        """
        self._ensure_ssc_set()

        if self.force_ansi is True or self.stream_supports_color is True:
            return (constants.COLOR_FORMAT_DEFAULTS | _format_defaults(self.default_keys)
                    | _palette.parse_palettes(record.levelno, self.palettes)
                    | self.defaults | record.__dict__)
        
        if self.stream_supports_color is False and self.backup_fmts is None:
            # no colors applied
            return (constants.COLOR_FORMAT_DEFAULTS | _format_defaults(self.default_keys)
                    | self.defaults | record.__dict__)
        
        # if we have a backup format and the stream does not support color
        return self.defaults | record.__dict__

    def formatException(self, exc_info: tuple, leveno: int) -> str:
        with io.StringIO() as sio:
            traceback.print_exception(*exc_info, limit=None, file=sio)
            s = sio.getvalue()
        if s[-1:] == "\n":
            s = s[:-1]
        
        if self.force_ansi is False and self.stream_supports_color is False:
            return s
        
        exc_text_palette = self.palettes.get("exc_text", None)
        if exc_text_palette is None:
            return s
        
        exc_text_c_enter = exc_text_palette.enter(leveno)
        exc_text_c_exit = exc_text_palette.exit(leveno)
        
        return f"{exc_text_c_enter}{s}{exc_text_c_exit}"

    def usesTime(self, fmt: str) -> bool:
        return fmt.find(logging.StrFormatStyle.asctime_search) >= 0

    def formatMessage(self, fmt: str, record: logging.LogRecord) -> str:
        kwargs = self._get_fmt_kwargs(record)
        try:
            return fmt.format(**kwargs)
        except KeyError as exc:
            raise ValueError(f"Formatting field not found in record: {exc!a}")
        
    def format(self, record: logging.LogRecord) -> str:
        record.message = record.getMessage()
        fmt = self._get_fmt_str(record.levelno)
        
        # set record's time only if "{asctime" is found in the format string
        if self.usesTime(fmt):
            record.asctime = self.formatTime(record, self.datefmt)
        
        # initial message format
        s = self.formatMessage(fmt, record)

        # custom format for exceptions (requires record.leveno to be passed)
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info, record.levelno)

                # remove the cache layer
                record.exc_info = None

        # the rest of this is default
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + record.exc_text
        if record.stack_info:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + self.formatStack(record.stack_info)
        return s
