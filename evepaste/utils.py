"""
evepaste.utils
~~~~~~~~~~~~~~
Utilities and re-usable helper functions for evepaste

"""
from functools import wraps


def split_and_strip(s):
    """
    Strip each line and split by new line. Also, removes empty lines

    :param str string: String to be split and stripped
    """
    # Strip each line
    lines = [line.strip(' ').replace(u"\xa0", u"").replace(u"\xc2", u"")
             for line in s.strip(' ').replace("\r\n", "\n").split('\n')]
    # Return non-empty lines
    return [line for line in lines if line]


def regex_match_lines(regex, lines):
    """
    Performs a regex search on each line and returns a list of matched groups
    and a list of lines which didn't match.

    :param regex regex: String to be split and stripped
    :param list lines: A list of strings to perform the regex on.
    """
    matches = []
    bad_lines = []
    for line in lines:
        match = regex.search(line)
        if match:
            matches.append(match.groups())
        else:
            bad_lines.append(line)
    return matches, bad_lines


def f_int(num):
    """ Converts a given numeric string into an integer

    :param string num: A string of the format "123,456", "123 456" or "123456"
    """
    if num is None:
        return
    try:
        return int(num.replace(',', '').replace('.', '').replace(' ', ''))
    except ValueError:
        return 0


def unpack_string(funct):
    """ This allows parsers to be passed a single string instead of a list of
        strings. The raw parsers take in a list of strings. This is to enable
        the ability to parse input that is of multiple types by chaining
        bad_lines into multiple parsers.
    """
    @wraps(funct)
    def wrapper(paste_string):
        return funct(split_and_strip(paste_string))

    return wrapper
