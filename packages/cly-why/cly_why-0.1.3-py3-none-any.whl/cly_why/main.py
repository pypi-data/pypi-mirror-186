import os
import re
import sys
import typing


def colorize(string: str, color: str="RED"):
    """ ANSI color codes """
    color = color.upper()
    ansi = {
        "BLACK": "\033[0;30m",
        "RED": "\033[0;31m",
        "GREEN": "\033[0;32m",
        "BROWN": "\033[0;33m",
        "BLUE": "\033[0;34m",
        "PURPLE": "\033[0;35m",
        "CYAN": "\033[0;36m",
        "LIGHT_GRAY": "\033[0;37m",
        "DARK_GRAY": "\033[1;30m",
        "LIGHT_RED": "\033[1;31m",
        "LIGHT_GREEN": "\033[1;32m",
        "YELLOW": "\033[1;33m",
        "LIGHT_BLUE": "\033[1;34m",
        "LIGHT_PURPLE": "\033[1;35m",
        "LIGHT_CYAN": "\033[1;36m",
        "LIGHT_WHITE": "\033[1;37m",
        "END": "\033[0m"
    }
    color_ansi = ansi[color]
    if color_ansi is None:
        color_ansi = ansi["RED"]
    endd = ansi["END"]
    return f"{color_ansi}{string}{endd}"

def text_decorate(string: str, decoration: str="BOLD"):
    decoration = decoration.upper()
    ansi = {
        "BOLD": "\033[1m",
        "FAINT": "\033[2m",
        "ITALIC": "\033[3m",
        "UNDERLINE": "\033[4m",
        "BLINK": "\033[5m",
        "NEGATIVE": "\033[7m",
        "CROSSED": "\033[9m",
        "END": "\033[0m"
    }
    text_dec = ansi[decoration]
    if text_dec is None:
        text_dec = ansi["BOLD"]

    endd = ansi["END"]
    return f"{text_dec}{string}{endd}"

def get_funcs(ignore_char: str="_"):
    funcs = []
    for key, value in globals().items():
        if callable(value) and value.__module__ == __name__ and not re.match(f"^{ignore_char}.*", key):
                funcs.append(value)
    return funcs

def clean_args(args: list) -> list:
    """Convert items to strings and replace hyphens with underscores """
    def a(x):
        return str(x).replace("-", "_")
    return list(map(a, args))

def cli_help(cmd=None):
    print(colorize(text_decorate("TESTING", "italic")))
    if cmd is not None:
        print(cmd.__doc__)
    else:
        print("Test")

def has_args(type_dict: dict, args: list):
    if len(type_dict) == 1 and "return" in type_dict:
        return True
    elif len(type_dict) == 0:
        err_mesg = "All cmds REQUIRE return type hints"
        print(err_mesg)
        return False, err_mesg
    else:
        print(type_dict)
        return True

def cly(args: list, def_cmd=cli_help, ignore_char: str="_", is_main: bool=False):
    if __name__ in ["__main__", args[0]] or is_main:
        try:
            if len(args) == 1:
                def_cmd()
                return True

            c_args = clean_args(args)
            sub_cmds = get_funcs(ignore_char=ignore_char)
            cmd = list(filter(lambda x: (x.__name__ in c_args), sub_cmds))
            if len(cmd) == 1:
                s_cmd = cmd[0]
                type_cmd = typing.get_type_hints(s_cmd)
                has_args(type_cmd, args[1:])
            else:
                print(args, "doesn't contain a valid sub_cmd")
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        return False, "Not run as main or app name"


def border(border_char: str="="):
    bord = "".join([border_char for _ in range(0, os.get_terminal_size().columns - 2)])
    print(f"+{bord}+")

cly(sys.argv)
