"""
evepaste.parsers.killmail
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse killmail.

"""
import re

from evepaste.exceptions import Unparsable
from evepaste.utils import f_int


TIME_RE = re.compile(r"^(\d\d\d\d.\d\d.\d\d \d\d:\d\d:\d\d)$")
PLAYER_RE = re.compile(r"^([\w ]+): ([\S ]+)$")
INVOLVED_RE = re.compile(r"^([\w ]+): ([\S ]+?)( \(laid the final blow\))?$")
ITEM_RE = re.compile(r"^([\w ]+)(, Qty: (\d+))?( \(([\w ]+)\))?$")


def parse_killmail(lines):
    """ Parse killmail format

    :param string paste_string: A killmail string
    """
    results = {}

    offset = 0
    next_state = parse_time_data
    iterations = 0
    while next_state and iterations < 100000:
        next_state, offset = next_state(lines, offset, results)
        iterations += 1

    return results, []


def parse_time_data(lines, offset, results):
    for i, line in enumerate(lines[offset:]):
        if i == 0:
            if not TIME_RE.search(line):
                raise Unparsable('Missing datetime.')

            results['time'] = line
        else:
            return parse_victim_data, offset + i
    raise Unparsable('Failed to parse past time.')


def parse_victim_data(lines, offset, results):
    victim_data = {}
    results['victim'] = victim_data
    for i, line in enumerate(lines[offset:]):
        transition = common_transitions(line)
        if transition:
            return transition, offset + i + 1
        else:
            match = PLAYER_RE.search(line)
            if match:
                key, val = match.groups()
                victim_data[format_key(key)] = val
            else:
                raise Unparsable('Failed parsing at line %s: %s'
                                 % (offset + i, line))
    return None, 0


def parse_involved_data(lines, offset, results):
    player = {}
    transition = None
    for i, line in enumerate(lines[offset:]):
        offset += 1
        transition = common_transitions(line)
        if player and line.startswith('Name:'):
            offset -= 1
            transition = parse_involved_data

        if transition:
            break
        else:
            match = INVOLVED_RE.search(line)
            if match:
                key, val, killing_blow = match.groups()
                player[format_key(key)] = val
                if killing_blow:
                    player['killing_blow'] = True
            else:
                raise Unparsable('Failed parsing at line %s: %s'
                                 % (offset, line))

    if transition:
        if 'involved' not in results:
            results['involved'] = []

        if player:
            player['killing_blow'] = player.get('killing_blow', False)
            player['damage_done'] = int(player.get('damage_done', 0))
            results['involved'].append(player)
    return transition, offset


def parse_destroyed_items(lines, offset, results):
    destroyed = []
    results['destroyed'] = destroyed
    transition = None
    for i, line in enumerate(lines[offset:]):
        transition = common_transitions(line)
        if transition:
            break
        else:
            match = ITEM_RE.search(line)
            if match:
                name, _, quantity, _, location = match.groups()
                destroyed.append({'name': name,
                                  'quantity': f_int(quantity) or 1,
                                  'location': location})
            else:
                raise Unparsable('Failed parsing at line %s: %s'
                                 % (offset + i, line))

    return transition, offset + i + 1


def parse_dropped_items(lines, offset, results):
    dropped = []
    results['dropped'] = dropped
    for i, line in enumerate(lines[offset:]):
        match = ITEM_RE.search(line)
        if match:
            name, _, quantity, _, location = match.groups()
            dropped.append({'name': name,
                            'quantity': quantity,
                            'location': location})
        else:
            raise Unparsable('Failed parsing at line %s: %s'
                             % (offset + i, line))
    return None, 0


def common_transitions(line):
    if line == 'Involved parties:':
        return parse_involved_data
    elif line == 'Destroyed items:':
        return parse_destroyed_items
    elif line == 'Dropped items:':
        return parse_dropped_items


def format_key(key):
    return key.lower().replace(' ', '_')
