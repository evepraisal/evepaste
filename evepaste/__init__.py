"""
evepaste
~~~~~~~~
A library to help parse out copy/pastable data from Eve Online.
"""

from evepaste.parsers import (parse_cargo_scan,
                              parse_fitting,
                              parse_eft,
                              parse_dscan,
                              parse_loot_history,
                              parse_contract,
                              parse_assets,
                              parse_bill_of_materials,
                              parse_manufacturing)
from evepaste.exceptions import Unparsable


def parse(paste_string):
    """ Tries out a series a parsers on a peice of text. This will return the
        first result with no errored lines. This should only be used if the
        format of paste_string is unknown. If it is known it is best to use the
        specific parser for the input.
    """
    for name, parser in (('bill_of_materials', parse_bill_of_materials),
                         ('loot_history', parse_loot_history),
                         ('dscan', parse_dscan),
                         ('eft', parse_eft),
                         ('fitting', parse_fitting),
                         ('contract', parse_contract),
                         ('assets', parse_assets),
                         ('cargo_scan', parse_cargo_scan)):
        try:
            result, bad_lines = parser(paste_string)
            if result and not bad_lines:
                return {'type': name,
                        'result': result,
                        'bad_lines': bad_lines}
        except Unparsable:
            pass

    raise Unparsable('No parser')


__all__ = ['parse',
           'parse_cargo_scan',
           'parse_eft',
           'parse_dscan',
           'parse_loot_history',
           'parse_contract',
           'parse_assets',
           'parse_bill_of_materials',
           'parse_fitting',
           'parse_manufacturing']

__version__ = '0.1'
