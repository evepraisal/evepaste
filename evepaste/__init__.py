"""
evepaste
~~~~~~~~
A library to help parse out copy/pastable data from Eve Online.

Usage:

    >>> import evepaste
    >>> evepaste.parse('10 Cargo Scanner II')
    ('cargo_scan', [{'name': 'Cargo Scanner II', 'quantity': 10}], [])

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
parse_cargo_scan = unpack_string(parsers.parse_cargo_scan)
parse_chat = unpack_string(parsers.parse_chat)
parse_contract = unpack_string(parsers.parse_contract)
parse_dscan = unpack_string(parsers.parse_dscan)
parse_eft = unpack_string(parsers.parse_eft)
parse_fitting = unpack_string(parsers.parse_fitting)
parse_killmail = unpack_string(parsers.parse_killmail)
parse_listing = unpack_string(parsers.parse_listing)
parse_loot_history = unpack_string(parsers.parse_loot_history)
parse_pi = unpack_string(parsers.parse_pi)
parse_survey_scanner = unpack_string(parsers.parse_survey_scanner)
parse_view_contents = unpack_string(parsers.parse_view_contents)
parse_wallet = unpack_string(parsers.parse_wallet)

PARSER_TABLE = [('bill_of_materials', parsers.parse_bill_of_materials),
                ('loot_history', parsers.parse_loot_history),
                ('survey_scanner', parsers.parse_survey_scanner),
                ('pi', parsers.parse_pi),
                ('dscan', parsers.parse_dscan),
                ('killmail', parsers.parse_killmail),
                ('chat', parsers.parse_chat),
                ('eft', parsers.parse_eft),
                ('fitting', parsers.parse_fitting),
                ('contract', parsers.parse_contract),
                ('assets', parsers.parse_assets),
                ('view_contents', parsers.parse_view_contents),
                ('wallet', parsers.parse_wallet),
                ('cargo_scan', parsers.parse_cargo_scan)]


def parse(paste_string, parsers=None):
    """ Tries out a series of parsers on a peice of text. This will return the
        first result with no errored lines. This should only be used if the
        format of paste_string is unknown. If it is known it is best to use the
        specific parser for the input.

    :param str paste_string: A string of text pasted from somewhere in
                             Eve Online.
    :param list parsers: A list of parsers. Defaults to a list of all of them
    """
    parsers = parsers or PARSER_TABLE
    lines = split_and_strip(paste_string)
    for name, parser in parsers:
        try:
            result, bad_lines = parser(lines)
            if result:
                return (name, result, bad_lines)
        except Unparsable:
            pass

    raise Unparsable('No valid parser found for the given text.')


__all__ = ['parse',
           'Unparsable',
           'parse_assets',
           'parse_bill_of_materials',
           'parse_cargo_scan',
           'parse_contract',
           'parse_dscan',
           'parse_eft',
           'parse_fitting',
           'parse_killmail',
           'parse_loot_history',
           'parse_pi',
           'parse_survey_scanner',
           'parse_view_contents',
           'parse_wallet']

__version__ = '0.6'
