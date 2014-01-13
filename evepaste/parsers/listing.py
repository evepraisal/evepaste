"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings including cargo scan results and normal human-readable lists.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int


# 10 x Cargo Scanner II | 10x Cargo Scanner II | 10 Cargo Scanner II
LISTING_RE = re.compile(r"^([\d,\.]+?) ?x? ([\S ]+)$")
# Cargo Scanner II x10 | Cargo Scanner II x 10 | Cargo Scanner II 10
LISTING_RE2 = re.compile(r"^([\S ]+?) x? ?([\d,\.]+)$")
# Cargo Scanner II
LISTING_RE3 = re.compile(r"^([\S ]+)$")


def parse_listing(lines):
    """ Parse Listing and Cargo Scan Results

    :param string paste_string: A raw string pasted from Eve Online of a cargo
                         scan result or a human listing
    """
    matches, bad_lines = regex_match_lines(LISTING_RE, lines)
    matches2, bad_lines2 = regex_match_lines(LISTING_RE2, bad_lines)
    matches3, bad_lines3 = regex_match_lines(LISTING_RE3, bad_lines2)

    items = defaultdict(int)

    for count, name in matches:
        items[name.strip()] += f_int(count) or 1

    for name, count in matches2:
        items[name.strip()] += f_int(count) or 1

    for res in matches3:
        items[res[0].strip()] += 1

    results = []
    for name, quantity in sorted(items.items()):
        results.append({'name': name, 'quantity': quantity})

    return results, bad_lines3
