"""
evepaste
~~~~~~~~
A library to help parse out copy/pastable data from Eve Online.

Usage:

    >>> import evepaste
    >>> evepaste.parse('10 Cargo Scanner II')
    {'bad_lines': [],
     'result': [{'name': 'Cargo Scanner II', 'quantity': 10}],
     'type': 'listing'}

    >>> evepaste.parse('''[Rifter, Fleet Tackle]
    ... Nanofiber Internal Structure I
    ... Nanofiber Internal Structure I
    ... Overdrive Injector System I
    ...
    ... Stasis Webifier I
    ... Warp Disruptor I
    ... 1MN Microwarpdrive I
    ...
    ... 200mm AutoCannon I, EMP S
    ... 200mm AutoCannon I, EMP S
    ... 200mm AutoCannon I, EMP S
    ... [empty high slot]''')
    {'bad_lines': [],
     'result': {'modules': [{'ammo': 'EMP S', 'name': '200mm AutoCannon I'},
                            {'ammo': 'EMP S', 'name': '200mm AutoCannon I'},
                            {'ammo': 'EMP S', 'name': '200mm AutoCannon I'},
                            {'name': 'Nanofiber Internal Structure I'},
                            {'name': 'Nanofiber Internal Structure I'},
                            {'name': 'Overdrive Injector System I'},
                            {'name': 'Stasis Webifier I'},
                            {'name': 'Warp Disruptor I'},
                            {'name': '1MN Microwarpdrive I'}],
                'name': 'Fleet Tackle',
                'ship': 'Rifter'},
     'type': 'eft'}
"""

from evepaste.parsers.assets import parse_assets
from evepaste.parsers.bill_of_materials import parse_bill_of_materials
from evepaste.parsers.contract import parse_contract
from evepaste.parsers.dscan import parse_dscan
from evepaste.parsers.eft import parse_eft
from evepaste.parsers.fitting import parse_fitting
from evepaste.parsers.listing import parse_listing
from evepaste.parsers.loot_history import parse_loot_history

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
                         ('listing', parse_listing)):
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
           'parse_assets',
           'parse_bill_of_materials',
           'parse_contract',
           'parse_dscan',
           'parse_eft',
           'parse_fitting',
           'parse_listing',
           'parse_loot_history']

__version__ = '0.1'
