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

# all valid flags for logging.LogRecord
# "message" and "asctime" are added by logging.Formatter.format
# "enter" and "exit" and custom flags used for color formatting
VALID_FLAGS = ["name", "message", "args", "levelname", "levelno", "pathname", "filename", "module",
               "exc_info", "exc_text", "stack_info", "lineno", "funcName", "created", "msecs",
               "relativeCreated", "thread", "threadName", "processName", "process", "asctime",
               "enter", "exit"]


COLOR_FORMAT_DEFAULTS = {
    f"name{chr(2)}": "",
    f"name{chr(3)}": "",
    f"message{chr(2)}": "",
    f"message{chr(3)}": "",
    f"args{chr(2)}": "",
    f"args{chr(3)}": "",
    f"levelname{chr(2)}": "",
    f"levelname{chr(3)}": "",
    f"levelno{chr(2)}": "",
    f"levelno{chr(3)}": "",
    f"pathname{chr(2)}": "",
    f"pathname{chr(3)}": "",
    f"filename{chr(2)}": "",
    f"filename{chr(3)}": "",
    f"module{chr(2)}": "",
    f"module{chr(3)}": "",
    f"exc_info{chr(2)}": "",
    f"exc_info{chr(3)}": "",
    f"exc_text{chr(2)}": "",
    f"exc_text{chr(3)}": "",
    f"stack_info{chr(2)}": "",
    f"stack_info{chr(3)}": "",
    f"lineno{chr(2)}": "",
    f"lineno{chr(3)}": "",
    f"funcName{chr(2)}": "",
    f"funcName{chr(3)}": "",
    f"created{chr(2)}": "",
    f"created{chr(3)}": "",
    f"msecs{chr(2)}": "",
    f"msecs{chr(3)}": "",
    f"relativeCreated{chr(2)}": "",
    f"relativeCreated{chr(3)}": "",
    f"thread{chr(2)}": "",
    f"thread{chr(3)}": "",
    f"threadName{chr(2)}": "",
    f"threadName{chr(3)}": "",
    f"processName{chr(2)}": "",
    f"processName{chr(3)}": "",
    f"process{chr(2)}": "",
    f"process{chr(3)}": "",
    f"asctime{chr(2)}": "",
    f"asctime{chr(3)}": "",
}
