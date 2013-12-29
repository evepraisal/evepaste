"""
eve_paste.utils
~~~~~~~~~~~~~~~
Utilities and re-usable helper functions for evepaste

"""


def split_and_strip(string):
    # Strip each line
    lines = [line.strip() for line in string.strip().split('\n')]
    # Return non-empty lines
    return [line for line in lines if line]


def regex_match_lines(regex, lines):
    matches = []
    bad_lines = []
    for line in lines:
        match = regex.search(line)
        if match:
            matches.append(match.groups())
        else:
            bad_lines.append(line)
    return matches, bad_lines
