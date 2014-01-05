"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings including cargo scan results and normal human-readable lists.

"""
import re

from evepaste.utils import regex_match_lines, f_int


# 10 x Cargo Scanner II | 10x Cargo Scanner II | 10 Cargo Scanner II
LISTING_RE = re.compile(r"^([\d ,\.]+) ?x? ([\S ]+)$")
# Cargo Scanner II x10 | Cargo Scanner II x 10
LISTING_RE2 = re.compile(r"^([\S ]+) x ?([\d ,\.]+)$")
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

    result = ([{'name': name.strip(), 'quantity': f_int(count) or 1}
               for count, name in matches] +
              [{'name': name.strip(),
                'quantity': f_int(count) or 1} for name, count in matches2] +
              [{'name': name[0], 'quantity': 1} for name in matches3])

    for item in result:
        if item['name'].endswith(' (Copy)'):
            item['details'] = 'BLUEPRINT COPY'
            item['name'] = item['name'].replace(' (Copy)', '')
        if item['name'].endswith(' (Original)'):
            item['details'] = 'BLUEPRINT ORIGINAL'
            item['name'] = item['name'].replace(' (Original)', '')

    return result, bad_lines3
