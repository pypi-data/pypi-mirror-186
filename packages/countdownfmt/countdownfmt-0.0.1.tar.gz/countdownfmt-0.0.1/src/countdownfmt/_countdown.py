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
from . import constants
from . import types
import datetime
import plogging
import logging
import inspect
import string
import typing
str_formatter = string.Formatter()
del string


plural_flag_to_plural = {
    "p": "s",
    "P": "S",
    "ep": "es",
    "eP": "eS",
    "Ep": "Es",
    "EP": "ES",
}


log_flag = plogging.setup_new("Flag", level=logging.INFO, package=__name__)
log_flags = plogging.setup_new("Flags", level=logging.INFO, package=__name__)
log_formatter = plogging.setup_new("Formatter", level=logging.INFO, package=__name__)


class Flag:
    __slots__ = ("name", "plural_specifiers", "extras")
    def __init__(self, name: str) -> None:
        log_flag.debug(f"Creating flag: '{name}'")
        self.name = name
        self.plural_specifiers: set[str] = set()
        self.extras: set[str] = set()

    def get_plurals(self) -> dict[str, str]:
        log_flag.debug(f"Acquiring converted plural specifiers for flag: '{self.name}'")
        plurals = {f"{self.name}_{spec}": plural_flag_to_plural[spec]
                   for spec in self.plural_specifiers}
        log_flag.debug(f"Acquired converted plural specifiers for flag: '{self.name}' -> {plurals}")
        return plurals
    
    def get_empty_plurals(self) -> dict[str, str]:
        log_flag.debug(f"Acquiring empty plural specifiers for flag: '{self.name}'")
        plurals = {f"{self.name}_{spec}": "" for spec in self.plural_specifiers}
        log_flag.debug(f"Acquired empty plural specifiers for flag: '{self.name}' -> {plurals}")
        return plurals

    def get_extras(self, defaults: dict) -> tuple[dict[str, str], dict[str, typing.Callable]]:
        kwargs: dict[str, str] = {}
        funcs: dict[str, typing.Callable] = {}
        log_flag.debug(f"Acquiring extras for flag: '{self.name}' with defaults: {defaults}")
        for ext in self.extras:
            try:
                d = defaults[ext]
                if inspect.isfunction(d):
                    funcs[ext] = d
                else:
                    kwargs[ext] = d
            except KeyError as exc:
                raise KeyError(f"Missing default: {ext}") from exc
        log_flag.debug(f"Acquired extras for flag: '{self.name}' -> kwargs={kwargs}, funcs={funcs}")
        return kwargs, funcs
    
    def get_empty_extras(self) -> dict[str, str]:
        log_flag.debug(f"Acquiring empty extras for flag: '{self.name}'")
        extras = {ext: "" for ext in self.extras}
        log_flag.debug(f"Acquired empty extras for flag: '{self.name}' -> {extras}")
        return extras

    def get_empty_kwargs(self) -> dict[str, str]:
        log_flag.debug(f"Acquiring empty kwargs for flag: '{self.name}'")
        kwargs = {self.name: ""}
        kwargs.update(self.get_empty_plurals())
        kwargs.update(self.get_empty_extras())
        log_flag.debug(f"Acquired empty kwargs for flag: '{self.name}' -> {kwargs}")
        return kwargs


class Flags(list[Flag]):
    def __contains__(self, other: Union[str, Flag]) -> bool:
        if isinstance(other, Flag):
            other = other.name
        for f in self:
            if f.name == other:
                return True
        return False
    
    def __getitem__(self, index: Union[str, Flag, int]) -> Flag:
        if isinstance(index, int):
            return super().__getitem__(index)

        if isinstance(index, Flag):
            index = index.name
        for f in self:
            if f.name == index:
                return f
        raise KeyError
    
    @typing.overload
    def get(self, index: Union[str, Flag, int]) -> Flag: ...
    @typing.overload
    def get(self, index: Union[str, Flag, int], default: types.T) -> Union[Flag, types.T]: ...
    def get(self, index: Union[str, Flag, int], default = types.MISSING):
        if default is types.MISSING:
            log_flag.debug(f"Acquiring flag by index: {index}")
            return self[index]
        log_flag.debug(f"Acquiring flag by index: {index} with default: {default}")
        try:
            return self[index]
        except KeyError:
            return default


def update_format_string(fmt: types.SupportsBracketFormat
                         ) -> tuple[Flags, types.SupportsBracketFormat]:
    data: list[str] = []
    flags: Flags = Flags()

    for literal_text, field_name, format_spec, conversion in str_formatter.parse(fmt):
        if literal_text:
            data.append(literal_text)
        
        # usually only happens at the very end if there is leftover text
        if field_name is None and format_spec is None and conversion is None:
            continue
        
        _conversion = f"!{conversion}" if conversion else ""
        _format_spec = f":{format_spec}" if format_spec else ""
        
        if not field_name:
            data.append(f"{{{_conversion}{_format_spec}}}")
            continue
        
        if field_name in constants.SKIPPED_FLAGS:
            data.append(f"{{{field_name}{_conversion}{_format_spec}}}")
            continue
        
        if field_name in constants.VALID_PLURAL_FLAGS and flags:
            flags[-1].plural_specifiers.add(field_name)
            data.append(f"{{{flags[-1].name}_{field_name}{_conversion}{_format_spec}}}")
            continue

        if field_name in constants.VALID_FLAGS:
            if field_name not in flags:
                flags.append(Flag(field_name))
            data.append(f"{{{field_name}{_conversion}{_format_spec}}}")
            continue
        
        if not flags:
            raise ValueError(f"Invalid flag: {field_name}")
        
        flags[-1].extras.add(field_name)
        data.append(f"{{{field_name}{_conversion}{_format_spec}}}")


    return (flags, "".join(data))


class Formatter:
    def __init__(self, fmt: types.SupportsBracketFormat, remove_empty: bool = True,
                 strip: bool = True, max_value: int = None, **defaults) -> None:
        log_formatter.debug(f"Updating format string: '{fmt}'")
        self.flags, self.fmt = update_format_string(fmt)
        self.remove_empty = remove_empty
        self.strip = strip
        self.max_value = max_value
        self.defaults = defaults
    
    @staticmethod
    def default_formatter() -> "Formatter":
        """Create and return the default formatter.
        
        """
        log_formatter.debug("Creating default formatter")
        return Formatter("T{z}{w}{wd}{d}{dd}{h}{hd}{m}{md}{s}{sd}", wd="w ", dd="d ", hd="h ",
                         md="m ", sd="s ")

    @staticmethod
    def _get_weeks(microseconds: int) -> tuple[int, int]:
        """Return the number of weeks and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring weeks from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_WEEK)
    
    @staticmethod
    def _get_days(microseconds: int) -> tuple[int, int]:
        """Return the number of days and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring days from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_DAY)
    
    @staticmethod
    def _get_hours(microseconds: int) -> tuple[int, int]:
        """Return the number of hours and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring hours from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_HOUR)
    
    @staticmethod
    def _get_minutes(microseconds: int) -> tuple[int, int]:
        """Return the number of minutes and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring minutes from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_MINUTE)
    
    @staticmethod
    def _get_seconds(microseconds: int) -> tuple[int, int]:
        """Return the number of seconds and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring seconds from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_SECOND)
    
    @staticmethod
    def _get_milliseconds(microseconds: int) -> tuple[int, int]:
        """Return the number of milliseconds and microseconds remaining given a number of starting
        microseconds.
        
        """
        log_formatter.debug(f"Acquiring milliseconds from microseconds: {microseconds}")
        return divmod(microseconds, constants.MICROSECONDS_IN_MILLISECOND)

    @staticmethod
    def _get_microseconds(microseconds: int) -> tuple[int, int]:
        """Return the number of microseconds and microseconds remaining given a number of starting
        microseconds.

        Equivalent to:
        `return microseconds, 1`
        
        """
        return microseconds, 1

    def format(self, microseconds: Union[int, float]) -> str:
        """The core method for formatting the format string with the given microseconds. All other
        format methods in `Formatter` convert to microseconds, then call this method.
        
        """
        log_formatter.debug(f"Formatting format string from microseconds: {microseconds}")
        z_flag = "+" if microseconds >= 0 else "-"
        remaining = abs(int(microseconds))
        funcs = {
            "w": (self._get_weeks, constants.MICROSECONDS_IN_WEEK),
            "d": (self._get_days, constants.MICROSECONDS_IN_DAY),
            "h": (self._get_hours, constants.MICROSECONDS_IN_HOUR),
            "M": (self._get_minutes, constants.MICROSECONDS_IN_MINUTE),
            "s": (self._get_seconds, constants.MICROSECONDS_IN_SECOND),
            "m": (self._get_milliseconds, constants.MICROSECONDS_IN_MILLISECOND),
            "u": (self._get_microseconds, 1),
        }

        fmt_kwargs = {"z": z_flag}
        values = {
            "w": None,
            "d": None,
            "h": None,
            "M": None,
            "s": None,
            "m": None,
            "u": None,
        }
        extra_funcs: dict[str, typing.Callable] = {}
        for flag_name, (func, mul) in funcs.items():
            flag: Flag = self.flags.get(flag_name, None)
            if flag:
                value, remaining = func(remaining)
                if self.max_value and value > self.max_value:
                    remaining += (value - self.max_value) * mul
                    value = self.max_value

                values[flag_name] = value

                if value == 0 and self.remove_empty:
                    fmt_kwargs.update(flag.get_empty_kwargs())
                    continue

                fmt_kwargs[flag_name] = value

                extra_kwargs, _extra_funcs = flag.get_extras(self.defaults)
                fmt_kwargs.update(extra_kwargs)
                extra_funcs.update(_extra_funcs)

                if value in [1, -1]:
                    fmt_kwargs.update(flag.get_empty_plurals())
                else:
                    fmt_kwargs.update(flag.get_plurals())
    
        values = list(values.values())
        for flag_name, func in extra_funcs.items():
            try:
                fmt_kwargs[flag_name] = func(*values)
            except Exception:
                fmt_kwargs[flag_name] = str(func)

        formatted = self.fmt.format(**fmt_kwargs)
        if self.strip:
            return formatted.strip()
        return formatted

    def format_time(self, weeks: Union[int, float] = None, days: Union[int, float] = None,
                    hours: Union[int, float] = None, minutes: Union[int, float] = None,
                    seconds: Union[int, float] = None, milliseconds: Union[int, float] = None,
                    microseconds: Union[int, float] = None) -> str:
        return self.format_timedelta(datetime.timedelta(weeks=weeks or 0, days=days or 0,
                                                        hours=hours or 0, minutes=minutes or 0,
                                                        seconds=seconds or 0,
                                                        milliseconds=milliseconds or 0,
                                                        microseconds=microseconds or 0))

    def format_microseconds(self, microseconds: Union[int, float]) -> str:
        """An alias for `.format`.
        
        """
    format_microseconds = format

    def format_milliseconds(self, milliseconds: Union[int, float]) -> str:
        """Format the format string given a number of seconds.
        
        """
        return self.format(milliseconds * constants.MICROSECONDS_IN_MILLISECOND)

    def format_seconds(self, seconds: Union[int, float]) -> str:
        """Format the format string given a number of seconds.
        
        """
        return self.format(seconds * constants.MICROSECONDS_IN_SECOND)

    def format_minutes(self, minutes: Union[int, float]) -> str:
        """Format the format string given a number of minutes.
        
        """
        return self.format(minutes * constants.MICROSECONDS_IN_MINUTE)

    def format_hours(self, hours: Union[int, float]) -> str:
        """Format the format string given a number of hours.
        
        """
        return self.format(hours * constants.MICROSECONDS_IN_HOUR)

    def format_days(self, days: Union[int, float]) -> str:
        """Format the format string given a number of days.
        
        """
        return self.format(days * constants.MICROSECONDS_IN_DAY)

    def format_weeks(self, weeks: Union[int, float]) -> str:
        """Format the format string given a number of weeks.
        
        """
        return self.format(weeks * constants.MICROSECONDS_IN_WEEK)
    
    def format_timedelta(self, td: datetime.timedelta) -> str:
        """Format the format string given a datetime.timedelta instance.
        
        """
        return self.format(td.total_seconds() * constants.MICROSECONDS_IN_SECOND)

    def format_datetime(self, dt: datetime.datetime, dt2: datetime.datetime = None) -> str:
        """Format the format string given a datetime object and an optional second datetime
        object. If the second datetime object is not provided, a new one will be created with the
        current time. The timedelta is acquired from `dt2 - dt`.
        
        """
        if dt2 is None:
            dt2 = datetime.datetime.now(tz=dt.tzinfo)
        td = dt2 - dt
        return self.format_timedelta(td)
