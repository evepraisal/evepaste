"""
evepaste.parsers.industry
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings for the industry interface.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int


# 10 Cargo Scanner II
INDUSTRY_RE = re.compile(r"^([\S ]+) \(([\d]+) Units?\)$")


def parse_industry(lines):
    """ Parse Industry

    :param string paste_string: A raw string pasted from the industry
    """
    matches, bad_lines = regex_match_lines(INDUSTRY_RE, lines)

    items = defaultdict(int)

    for name, count in matches:
        items[name.strip()] += f_int(count)

    results = []
    for name, quantity in sorted(items.items()):
        item = {'name': name, 'quantity': quantity}

        results.append(item)

    return results, bad_lines
