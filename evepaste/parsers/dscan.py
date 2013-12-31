"""
evepaste.parsers.dscan
~~~~~~~~~~~~~~~~~~~~~~
Parse d-scan results.

"""
import re

from evepaste.utils import split_and_strip, regex_match_lines


DSCAN_LIST_RE = re.compile(r"""^([\S ]*)\t  # name
                                ([\S ]*)\t  # type
                                ([\S ]*)$   # distance
                                """, re.X)


def parse_dscan(paste_string):
    """ Parse D-Scan format

    :param string paste_string: A D-Scan result string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(DSCAN_LIST_RE, paste_lines)

    result = [{'name': name, 'type': _type, 'distance': distance}
              for name, _type, distance in matches]
    return result, bad_lines
