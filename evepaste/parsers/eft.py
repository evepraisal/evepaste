"""
evepaste.parsers.eft
~~~~~~~~~~~~~~~~~~~~
Parse EFT blocks.

"""
import re

from evepaste.exceptions import Unparsable
from evepaste.utils import split_and_strip, regex_match_lines

# [Rifter, Title] | [Rifter,Title]
EFT_LIST_RE = re.compile(r"^([\S ]+), ?([\S ]+)$")
EFT_BLACKLIST = ['[empty high slot]',
                 '[empty low slot]',
                 '[empty medium slot]',
                 '[empty rig slot]']


def parse_eft(paste_string):
    """ Parse EFT format

    :param string paste_string: An EFT block string
    """
    paste_lines = split_and_strip(paste_string)

    for item in EFT_BLACKLIST:
        if item in paste_lines:
            paste_lines.remove(item)

    if not paste_lines:
        raise Unparsable('No valid parsable lines')

    if '[' not in paste_lines[0] or ']' not in paste_lines[0]:
        raise Unparsable('Invalid EFT title line')

    title_parts = paste_lines[0].strip('[]').split(',', 1)
    if len(title_parts) != 2:
        raise Unparsable('Invalid EFT title line')

    ship = title_parts[0].strip()
    eft_name = title_parts[1].strip()
    modules = []

    # Match "Module, Ammo"
    matches, bad_lines = regex_match_lines(EFT_LIST_RE, paste_lines[1:])

    for module, ammo in matches:
        modules.append({'name': module, 'ammo': ammo})

    for line in bad_lines:
        modules.append({'name': line})

    result = {'ship': ship.strip(),
              'name': eft_name.strip(),
              'modules': [res for res in modules]}
    return result, []
