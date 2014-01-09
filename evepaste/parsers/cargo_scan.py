"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings including cargo scan results and normal human-readable lists.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int


# 10 Cargo Scanner II
CARGO_SCAN_RE = re.compile(r"^([\d,\.]+) ([\S ]+)$")


def parse_cargo_scan(lines):
    """ Parse Cargo Scan Results

    :param string paste_string: A raw string pasted from Eve Online of a cargo
                         scan result
    """
    matches, bad_lines = regex_match_lines(CARGO_SCAN_RE, lines)

    items = defaultdict(int)

    for count, name in matches:
        items[name.strip()] += f_int(count) or 1

    results = []
    for name, quantity in sorted(items.items()):
        item = {'name': name, 'quantity': quantity}
        if item['name'].endswith(' (Copy)'):
            item['details'] = 'BLUEPRINT COPY'
            item['name'] = item['name'].replace(' (Copy)', '')
        if item['name'].endswith(' (Original)'):
            item['details'] = 'BLUEPRINT ORIGINAL'
            item['name'] = item['name'].replace(' (Original)', '')

        results.append(item)

    return results, bad_lines
