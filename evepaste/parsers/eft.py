"""
evepaste.parsers.eft
~~~~~~~~~~~~~~~~~~~~
Parse EFT blocks.

"""
import re
from collections import defaultdict

from evepaste.exceptions import Unparsable
from evepaste.utils import regex_match_lines
from evepaste.parsers.listing import parse_listing

# [Rifter, Title] | [Rifter,Title]
EFT_LIST_RE = re.compile(r"^([\S ]+), ?([\S ]+)$")
EFT_BLACKLIST = ['[empty high slot]',
                 '[empty low slot]',
                 '[empty medium slot]',
                 '[empty rig slot]',
                 '[empty subsystem slot]']


def parse_eft(lines):
    """ Parse EFT format

    :param string paste_string: An EFT block string
    """
    lines = [line for line in lines if line.lower() not in EFT_BLACKLIST]

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

    module_w_ammo = defaultdict(int)
    for module, ammo in matches:
        module_w_ammo[(module, ammo)] += 1

    for (name, ammo), quantity in sorted(module_w_ammo.items()):
        modules.append({'name': name, 'ammo': ammo, 'quantity': quantity})

    for item in matches2:
        modules.append(item)

    result = {'ship': ship,
              'name': eft_name,
              'modules': [res for res in modules]}
    return result, bad_lines2
