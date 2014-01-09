"""
evepaste.parsers.dscan
~~~~~~~~~~~~~~~~~~~~~~
Parse d-scan results.

"""
import re

from evepaste.utils import regex_match_lines


DSCAN_LIST_RE = re.compile(r"""^([\S ]*)\t                  # item name
                                ([\S ]*)\t                  # name
                                (([\d,\.]*\ (m|km|AU))|-)$  # distance
                                """, re.X)


def parse_dscan(lines):
    """ Parse D-Scan format

    :param string paste_string: A D-Scan result string
    """
    matches, bad_lines = regex_match_lines(DSCAN_LIST_RE, lines)

    result = [{'item_name': item_name, 'name': name, 'distance': distance}
              for item_name, name, distance, _, _ in matches]
    return result, bad_lines
