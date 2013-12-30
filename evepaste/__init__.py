"""
evepaste
~~~~~~~~
A library to help parse out copy/pastable data from Eve Online.
"""

from evepaste.parsers import (parse_cargo_scan,
                              parse_human_listing,
                              parse_eft,
                              parse_dscan,
                              parse_loot_history,
                              parse_contract,
                              parse_asset_list)

__all__ = ['parse_cargo_scan',
           'parse_human_listing',
           'parse_eft',
           'parse_dscan',
           'parse_loot_history',
           'parse_contract',
           'parse_asset_list']

__version__ = '0.1'
