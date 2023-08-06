# Install
`$ pip install plogging`

# Documentation
Pending... Until then, I will place some implementation code below. Before doing that, though, I
want to make a few notes on the format strings used in the formatter. Firstly, they must use the
*bracket* formatting style, e.g. `"{a}{b!r}{c:<3}"`. Secondly, by default, colors are only applied
to a given field, meaning for the format string `"Log time: {asctime}"`, only the time would be
given color. This can be changed by using the special `enter` and `exit` fields - for example:
`"{enter}Log time: {asctime}{exit}"`, which would cause the entire area to be formatted given the
palette for `asctime`. Any other normal fields can also be included within the `enter`/`exit`
fields, in which case the palette for the first field would be used. Additionally, any field
prefixed with an underscore (`_`) will not have any formatting applied to it, though the field name
will be reverted to the non-prefixed version (e.g. `_asctime` -> `asctime`).

```py
import plogging
import logging

# default formatter that shows a small amount of information (time,
# level name, logger name, message)
log = plogging.setup_new("logger", level=logging.DEBUG, package="test")

# the default formatter itself can be acquired as follows:
plogging.utils.default_formatter()

# you can also setup an existing logger for color formatting
log = logging.getLogger(...)
plogging.setup_existing(log, level=logging.DEBUG)

# custom formatters can also be created; here is an example:
formatter = plogging.Formatter(
    fmts=plogging.LevelContainer(
        debug="{asctime} {levelname:<8} {module} {message} [{threadname}, {processname}, "
              "{somethingelse}]",
        default="{asctime} {levelname:<8} {module} {message}"
    ),
    datefmt="%Y-%m-%d %H:%M:%S",
    defaults={
        "somethingelse": "somethingelse's value"
    },
    asctime=plogging.Palette(
        plogging.LevelContainer(
            default="30;1"
        )
    ),
    levelname=plogging.Palette(
        plogging.LevelContainer(
            "32;1",
            "34;1",
            "33;1",
            "31;1",
            "41"
        )
    )
)

log = plogging.setup_new("logger", level=logging.INFO, formatter=formatter)

```



