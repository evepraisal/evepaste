"""
eve_paste.parsers
~~~~~~~~~~~~~~~~~
Various parsers for string input which is copy/pastable from Eve Online.

"""
import re

from evepaste.exceptions import Unparsable

CARGO_SCAN_RE = re.compile(r"^(\d+) ([\S ]+)", re.MULTILINE)
HUMAN_LIST_RE = re.compile(r"^(\d+)?[x ]*([\S ]+)", re.MULTILINE)
EFT_LIST_RE = re.compile(r"^([A-Za-z0-9 ]+)", re.MULTILINE)
DSCAN_LIST_RE = re.compile(r"^([\S ]*)\t([\S ]*)\t([\S ]*)", re.MULTILINE)


def parse_cargo_scan(paste_string):
    """ Parse Cargo Scan Results

    :param string paste_string: A raw string pasted from Eve Online of a cargo
                                scan result.
    """
    matches = CARGO_SCAN_RE.findall(paste_string)
    return [{'name': name, 'quantity': int(count)} for count, name in matches]


def parse_human_listing(paste_string):
    """ Parse Human-readble List of items

    :param string paste_string: A new-line separated list of items
    """
    matches = HUMAN_LIST_RE.findall(paste_string)
    return [{'name': name, 'quantity': int(count or 1)}
            for count, name in matches]


def parse_eft(paste_string):
    first_line = paste_string.lstrip().split('\n')[0]
    title_parts = first_line.strip('[]').split(',', 1)
    if len(title_parts) != 2:
        raise Unparsable('Invalid EFT title line')

    ship, eft_name = first_line.strip('[]').split(',', 1)
    module_matches = EFT_LIST_RE.findall(paste_string)
    modules = [name for name in module_matches]

    return {'ship': ship.strip(),
            'name': eft_name.strip(),
            'modules': modules}


def parse_dscan(paste_string):
    matches = DSCAN_LIST_RE.findall(paste_string)
    return [{'name': name, 'type': _type, 'distance': distance}
            for name, _type, distance in matches]

# TODO: contracts
# TODO: Manufactoring
# TODO: Assets
# TODO: Inventory
# TODO: Bill of Materials
# TODO: Loot history
