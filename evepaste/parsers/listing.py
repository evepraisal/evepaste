"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings including cargo scan results and normal human-readable lists.

"""
import re

from evepaste.utils import split_and_strip, regex_match_lines, f_int


# 10 x Cargo Scanner II | 10x Cargo Scanner II | 10 Cargo Scanner II
LISTING_RE = re.compile(r"^([\d ,]+) ?x? ([\w ]+)$")
# Cargo Scanner II x10 | Cargo Scanner II 10
LISTING_RE2 = re.compile(r"^([\w ]+) x ?([\d ,]+)$")


def parse_listing(paste_string):
    """ Parse Listing and Cargo Scan Results

    :param string paste_string: A raw string pasted from Eve Online of a cargo
                                scan result or a human listing
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(LISTING_RE, paste_lines)
    matches2, bad_lines2 = regex_match_lines(LISTING_RE2, bad_lines)

    result = ([{'name': name.strip(), 'quantity': f_int(count)}
               for count, name in matches] +
              [{'name': name.strip(),
                'quantity': f_int(count or '1')} for name, count in matches2] +
              [{'name': name, 'quantity': 1} for name in bad_lines2])

    return result, []
