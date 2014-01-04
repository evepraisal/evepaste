"""
evepaste.parsers.eft
~~~~~~~~~~~~~~~~~~~~
Parse EFT blocks.

"""
import re

from evepaste.exceptions import Unparsable
from evepaste.utils import regex_match_lines
from evepaste.parsers.listing import parse_listing

# [Rifter, Title] | [Rifter,Title]
EFT_LIST_RE = re.compile(r"^([\S ]+), ?([\S ]+)$")
EFT_BLACKLIST = ['[empty high slot]',
                 '[empty low slot]',
                 '[empty medium slot]',
                 '[empty rig slot]']


def parse_eft(lines):
    """ Parse EFT format

    :param string paste_string: An EFT block string
    """
    for item in EFT_BLACKLIST:
        if item in lines:
            lines.remove(item)

    if not lines:
        raise Unparsable('No valid parsable lines')

    if '[' not in lines[0] or ']' not in lines[0]:
        raise Unparsable('Invalid EFT title line')

    title_parts = lines[0].strip('[]').split(',', 1)
    if len(title_parts) != 2:
        raise Unparsable('Invalid EFT title line')

    ship = title_parts[0].strip()
    eft_name = title_parts[1].strip()
    modules = []

    # Match "Module, Ammo"
    matches, bad_lines = regex_match_lines(EFT_LIST_RE, lines[1:])
    matches2, bad_lines2 = parse_listing(bad_lines)

    for module, ammo in matches:
        modules.append({'name': module, 'ammo': ammo})

    for item in matches2:
        modules.append(item)

    result = {'ship': ship.strip(),
              'name': eft_name.strip(),
              'modules': [res for res in modules]}
    return result, bad_lines2
