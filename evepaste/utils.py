"""
evepaste.utils
~~~~~~~~~~~~~~
Utilities and re-usable helper functions for evepaste

"""


def split_and_strip(string):
    """
    Strip each line and split by new line. Also, removes empty lines

    :param str string: String to be split and stripped
    """
    # Strip each line
    lines = [line.strip(' ') for line in string.strip(' ').split('\n')]
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
