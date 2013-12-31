"""
evepaste
~~~~~~~~
A library to help parse out copy/pastable data from Eve Online.

Usage:

    >>> import evepaste
    >>> evepaste.parse('10 Cargo Scanner II')
    ('listing', [{'name': 'Cargo Scanner II', 'quantity': 10}], [])

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
    ('eft',
     {'modules': [{'ammo': 'EMP S', 'name': '200mm AutoCannon I'},
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
     [])
"""
from evepaste import parsers
from evepaste.exceptions import Unparsable
from evepaste.utils import split_and_strip, unpack_string


# Add the ability for each supported parser take a string instead of a list of
# strings.
parse_assets = unpack_string(parsers.parse_assets)
parse_bill_of_materials = unpack_string(parsers.parse_bill_of_materials)
parse_contract = unpack_string(parsers.parse_contract)
parse_dscan = unpack_string(parsers.parse_dscan)
parse_eft = unpack_string(parsers.parse_eft)
parse_fitting = unpack_string(parsers.parse_fitting)
parse_listing = unpack_string(parsers.parse_listing)
parse_loot_history = unpack_string(parsers.parse_loot_history)


def parse(paste_string):
    """ Tries out a series of parsers on a peice of text. This will return the
        first result with no errored lines. This should only be used if the
        format of paste_string is unknown. If it is known it is best to use the
        specific parser for the input.

    :param str paste_string: A string of text pasted from somewhere in
                             Eve Online.
    """
    lines = split_and_strip(paste_string)
    for checker in (lambda res, bad_lines: result and not bad_lines,
                    lambda res, bad_lines: result):
        for name, parser in (('bill_of_materials',
                              parsers.parse_bill_of_materials),
                             ('loot_history', parsers.parse_loot_history),
                             ('dscan', parsers.parse_dscan),
                             ('eft', parsers.parse_eft),
                             ('fitting', parsers.parse_fitting),
                             ('contract', parsers.parse_contract),
                             ('assets', parsers.parse_assets),
                             ('listing', parsers.parse_listing)):
            try:
                result, bad_lines = parser(lines)
                if checker(result, bad_lines):
                    return (name, result, bad_lines)
            except Unparsable:
                pass

    raise Unparsable('No valid parser found for the given text.')


__all__ = ['parse',
           'Unparsable',
           'parse_assets',
           'parse_bill_of_materials',
           'parse_contract',
           'parse_dscan',
           'parse_eft',
           'parse_fitting',
           'parse_listing',
           'parse_loot_history']

__version__ = '0.1'
