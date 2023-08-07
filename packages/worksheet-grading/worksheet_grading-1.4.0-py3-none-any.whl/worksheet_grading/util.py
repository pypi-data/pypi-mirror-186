#!/usr/bin/env python

import colorama
import sys
from typing import Generator

# ========== LICENSE AND AUTHOR ========== #

from worksheet_grading.__init__ import __version__, __author__, __copyright__, __license__, __program__, __repository__, __package__


def version_string(program=__program__):
    return "\n".join([
        bright(light_blue(program)),
        f"Part of the {__package__} package version {__version__} <https://pypi.org/project/{__package__}/{__version__}>",
        "",
        bright(__copyright__),
        __license__,
        "",
        f"See <{__repository__}>",
    ])


# ========== TERMINAL COLOR ========== #

# Color configuration
COLOR = True

def set_color(color):
	global COLOR
	COLOR = color


def red(msg):
    if COLOR:
        return colorama.Fore.RED + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def green(msg):
    if COLOR:
        return colorama.Fore.GREEN + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def magenta(msg):
    if COLOR:
        return colorama.Fore.MAGENTA + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def yellow(msg):
    if COLOR:
        return colorama.Fore.YELLOW + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_red(msg):
    if COLOR:
        return colorama.Fore.LIGHTRED_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_yellow(msg):
    if COLOR:
        return colorama.Fore.LIGHTYELLOW_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_green(msg):
    if COLOR:
        return colorama.Fore.LIGHTGREEN_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_blue(msg):
    if COLOR:
        return colorama.Fore.LIGHTBLUE_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def dim(msg):
    return colorama.Style.DIM + str(msg) + colorama.Style.RESET_ALL


def bright(msg):
    return colorama.Style.BRIGHT + str(msg) + colorama.Style.RESET_ALL


def highlight(msg):
    return colorama.Back.LIGHTBLACK_EX + bright(str(msg)) + colorama.Back.RESET




# ========== UTILITY ========== #

def suffix_string(csv_name, suffix):
    return csv_name.replace(".csv", "") + suffix + ".csv"


def print_err(msg):
    sys.stderr.write(bright(red(msg)) + "\n")


def print_info(msg):
    print(magenta("INFO: " + str(msg)))


def print_warn(msg):
    print("WARN: " + str(msg))


def parse_int_list(string: str) -> Generator[int, None, None]:
    for s in string.split(","):
        if "-" in s:
            start, end = s.split("-")
            yield from range(int(start), int(end) + 1)
        else:
            yield int(s)


def get_next(cur: int, ints: list):
    for i in ints:
        if i > cur:
            return i
    return None


def get_prev(cur: int, ints: list):
    for i in reversed(ints):
        if i < cur:
            return i
    return None
