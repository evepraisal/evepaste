"""
evepaste.parsers
~~~~~~~~~~~~~~~~
Various parsers for string input which is copy/pastable from Eve Online.

"""
import re

from evepaste.exceptions import Unparsable
from evepaste.utils import split_and_strip, regex_match_lines, f_int

CARGO_SCAN_RE = re.compile(r"^([\d ,]+) ([\S ]+)$")
HUMAN_LIST_RE = re.compile(r"^([\d ,]+)[x ]+([\S ]+)$")
HUMAN_LIST_RE2 = re.compile(r"^([\S ]+) x ?([\d ,]+)$")
FITTING_BLACKLIST = ['High power',
                     'Medium power',
                     'Low power',
                     'Rig Slot',
                     'Sub System',
                     'Charges',
                     'Drones']
EFT_LIST_RE = re.compile(r"^([\S ]+)$")
EFT_LIST_RE2 = re.compile(r"^([\S ]+), ?([\S ]+)$")
EFT_BLACKLIST = ['[empty high slot]',
                 '[empty low slot]',
                 '[empty medium slot]',
                 '[empty rig slot]']
DSCAN_LIST_RE = re.compile(r"""^([\S ]*)\t  # name
                                ([\S ]*)\t  # type
                                ([\S ]*)$   # distance
                                """, re.X)
LOOT_HIST_RE = re.compile(
    r"(\d\d:\d\d:\d\d) ([\S ]+) has looted ([\d ,]+) x ([\S ]+)$")
CONTRACT_RE = re.compile(r"""^([\S ]*)\t  # name
                              (\d*)\t     # quantity
                              ([\S ]*)\t  # type
                              ([\S ]*)\t  # category
                              ([\S ]*)$   # info
                              """, re.X)
ASSET_LIST_RE = re.compile(r"""^([\S ]*)                    # name
                                (\t([\d ,]+))?              # quantity
                                (\t([\S ]*))?               # group
                                (\t([\S ]*))?               # category
                                (\t(Large|Medium|Small|))?  # size
                                (\t(High|Medium|Low|))?     # slot
                                (\t([\d ,]* m3))?           # volume
                                (\t([\d]+|))?               # meta level
                                (\t([\d])+|)?$              # tech level
                               """, re.X)
BOM_RE = re.compile(r"^([\S ]+) - \[You: (\d+) - Perfect: (\d+)\]$")
BOM_RE2 = re.compile(r"^([\S ]+) \[([\d]+)\]$")
MANUFACTURING_RE = re.compile(r"""^([\S ]*)\t   # name
                                   ([\d ,]*)\t  # quantity
                                   ([\S ]*)\t   # type
                                   ([\S ]*)\t   # category
                                   ([\S ]*)$    # info
                                   """, re.X)


def parse_cargo_scan(paste_string):
    """ Parse Cargo Scan Results

    :param string paste_string: A raw string pasted from Eve Online of a cargo
                                scan result.
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(CARGO_SCAN_RE, paste_lines)
    result = [{'name': name, 'quantity': f_int(count)}
              for count, name in matches]
    return result, bad_lines


def parse_human_listing(paste_string):
    """ Parse Human-readble List of items

    :param string paste_string: A new-line separated list of items
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(HUMAN_LIST_RE, paste_lines)
    matches2, bad_lines2 = regex_match_lines(HUMAN_LIST_RE2, bad_lines)

    result = ([{'name': name,
                'quantity': f_int(count or '1')} for count, name in matches] +
              [{'name': name,
                'quantity': f_int(count or '1')} for name, count in matches2] +
              [{'name': name, 'quantity': 1} for name in bad_lines2])

    return result, []


def parse_fitting_listing(paste_string):
    """ Parse Fitting List

    :param string paste_string: A new-line separated list of items
    """
    paste_lines = split_and_strip(paste_string)

    for item in FITTING_BLACKLIST:
        if item in paste_lines:
            paste_lines.remove(item)

    return parse_human_listing('\n'.join(paste_lines))


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

    title_parts = paste_lines[0].strip('[]').split(',', 1)
    if len(title_parts) != 2:
        raise Unparsable('Invalid EFT title line')

    ship = title_parts[0].strip()
    eft_name = title_parts[1].strip()
    modules = []

    # Match "Module, Ammo"
    matches, bad_lines = regex_match_lines(EFT_LIST_RE2, paste_lines[1:])

    for module, ammo in matches:
        modules.append({'name': module, 'ammo': ammo})

    # Match "Module"
    matches, bad_lines = regex_match_lines(EFT_LIST_RE, bad_lines)

    for res in matches:
        modules.append({'name': res[0]})

    result = {'ship': ship.strip(),
              'name': eft_name.strip(),
              'modules': [res for res in modules]}
    return result, bad_lines


def parse_dscan(paste_string):
    """ Parse D-Scan format

    :param string paste_string: A D-Scan result string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(DSCAN_LIST_RE, paste_lines)

    result = [{'name': name, 'type': _type, 'distance': distance}
              for name, _type, distance in matches]
    return result, bad_lines


def parse_loot_history(paste_string):
    """ Parse loot history format

    :param string paste_string: A loot history result string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(LOOT_HIST_RE, paste_lines)

    result = [{'time': time,
               'player_name': player_name,
               'quantity': f_int(quantity),
               'name': name}
              for time, player_name, quantity, name in matches]
    return result, bad_lines


def parse_contract(paste_string):
    """ Parse contract format

    :param string paste_string: A contract result string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(CONTRACT_RE, paste_lines)

    result = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'type': _type,
               'category': category,
               'info': info,
               'fitted': info.startswith('Fitted')}
              for name, quantity, _type, category, info in matches]
    return result, bad_lines


def parse_asset_list(paste_string):
    """ Parse asset list

    :param string paste_string: An asset list string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(ASSET_LIST_RE, paste_lines)

    result = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'group': group,
               'category': category,
               'size': size,
               'slot': slot,
               'volume': volume,
               'meta_level': meta_level,
               'tech_level': tech_level}
              for (name,
                   _, quantity,
                   _, group,
                   _, category,
                   _, size,
                   _, slot,
                   _, volume,
                   _, meta_level,
                   _, tech_level) in matches]
    return result, bad_lines


def parse_bill_of_materials(paste_string):
    """ Parse bill of materials

    :param string paste_string: A bill of material string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(BOM_RE, paste_lines)
    matches2, bad_lines2 = regex_match_lines(BOM_RE2, bad_lines)

    result = [{'name': name,
               'you': f_int(you),
               'perfect': f_int(perfect)}
              for name, you, perfect in matches]
    result2 = [{'name': name,
                'quantity': f_int(quantity)}
               for name, quantity in matches2]
    return result + result2, bad_lines2


def parse_manufacturing(paste_string):
    """ Parse manufacturing list

    :param string paste_string: A manufacturing list string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(MANUFACTURING_RE, paste_lines)

    result = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'type': _type,
               'category': category,
               'info': info}
              for name, quantity, _type, category, info in matches]
    return result, bad_lines
