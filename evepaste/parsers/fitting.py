"""
evepaste.parsers.fitting
~~~~~~~~~~~~~~~~~~~~~~~~
Parse saved fittings.

"""
from evepaste.exceptions import Unparsable
from evepaste.parsers.listing import parse_listing


FITTING_BLACKLIST = ['High power',
                     'Medium power',
                     'Low power',
                     'Rig Slot',
                     'Sub System',
                     'Charges',
                     'Drones']


def parse_fitting(lines):
    """ Parse Fitting List

    :param string paste_string: A new-line separated list of items
    """

    is_fitting_listing = False
    for item in FITTING_BLACKLIST:
        if item in lines:
            lines.remove(item)
            is_fitting_listing = True

    if is_fitting_listing is False:
        raise Unparsable('Not a fitting list')

    return parse_listing(lines)
