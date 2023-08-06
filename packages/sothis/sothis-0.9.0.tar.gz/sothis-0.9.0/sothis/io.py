"""
Author: Oliver B. Gaither
Date: 1/16/2023
Description: input/output helper functions
"""

from .helpers import isint, isfloat
from .nums import MAXINT32, MININT32, MAXINT64, MININT64


def getfloat(message, lo=MININT64, hi=MAXINT64):
    """
    get an floating point input from user from console
    :param message: input prompt
    :param bounds: possible min and max bounds for float
    :return: a valid floating point number
    """
    response = input(message)
    
    while (not isfloat(response)) or (float(response) > hi or float(response) < lo):
        if not isfloat(response):
            print("please enter an integer/floating-point number")
        if (isfloat(response)) and (float(response) not in bounds):
            print(f"response out of valid range. enter a number between {lo} and {hi}")
        response = input(message)
    return float(response)


def getint(message, bounds=None):
    """
    get an integer input from user from console
    :param message: input prompt
    :param bounds: possible min and max bounds for integer
    :return: a valid integer
    """
    if bounds == None:
        bounds = range(MININT64, MAXINT64)  # set bounds to be min int64 to max int64
    
    response = input(message)
    
    while (not isint(response)) or (int(response) not in bounds):
        if not isint(response):
            print("please enter an integer")
        if (isint(response)) and (int(response) not in bounds):
            print(f"integer out of valid range. enter a number between {bounds[0]} and {bounds[-1]}")
        response = input(message)
    return int(response)


def getstr(prompt, options=None):
    """
    get a string input from a user that
    can have a restricted set of options
    :param prompt: prompt for input
    :param options: optional restricted options for possible input
    :return: user input
    """
    if not options:
        return input(prompt)
    
    response = input(prompt)
    while response not in options:
        print("not a valid response")
        response = input(prompt)
    return response


def bold(text):
    """return a bolded version of text"""
    return f"\033[1m{text}\033[0m"


def add_color(text, color, background=False):
    """ add color to the text or background of the text """
    color = color.lower()
    COLORS = {
        "black": 30, "red": 31, "green": 32,
        "yellow": 33, "blue": 34, "purple": 35,
        "cyan": 36, "white": 37, "orange": "33;1"
    }
    if color not in COLORS:
        raise ValueError("add_color(): color %s not available" % color)
    if (background):
        for c in COLORS:
            COLORS[c] += 10
    
    return f"\u001b[{COLORS[color]}m{text}\u001b[0m"


def underline(text):
    """ add an underline to the text string """
    return f"\u001b[4m{text}\u001b[0m"


def decorate(text, color=None, undline=False, makebold=False):
    """
    a general function for decorating a string
    :param text: the string to decorate
    :param color: the color of text to change to
    :param undline: whether to underline the text or not
    :param makebold: whether to make the text bolded or not
    :return: a decorated string
    """
    if color:
        text = add_color(text, color)
    if (undline):
        text = underline(text)
    if (makebold):
        text = bold(text)
    return text


def rainbow(text: str) -> str:
    """
    returns a string converted into a rainbow
    :param text: a string
    :return: a string with ansi formmated colored characters
    """
    out = ""
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    numColors = len(colors)
    j = 0
    for c in text:
        out = out + add_color(c, color=colors[j % numColors])
        if c != ' ': j = j + 1
    
    return out
