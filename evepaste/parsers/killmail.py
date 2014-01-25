"""
evepaste.parsers.killmail
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse killmail.

"""
import re

from evepaste.exceptions import Unparsable
from evepaste.utils import f_int


TIME_RE = re.compile(r"^(\d\d\d\d.\d\d.\d\d \d\d:\d\d(:\d\d)?)$")
PLAYER_RE = re.compile(r"^([\w ]+): ([\S ]+)$")
INVOLVED_RE = re.compile(r"^([\w ]+): ([\S ]+?)( \(laid the final blow\))?$")
ITEM_RE = re.compile(r"^([\w '-]+?)(, Qty: (\d+))?( \(([\w ]+)\))?$")


def parse_killmail(lines):
    """ Parse killmail format

    :param string paste_string: A killmail string
    """
    results = {
        'involved': [],
        'destroyed': [],
        'dropped': []
    }

    result_map = {
        'time': set_value,
        'victim': set_value,
        'involved': append_value,
        'destroyed': append_value,
        'dropped': append_value,
    }

    offset, iterations = 0, 0
    next_state = parse_time_data

    while next_state and iterations < 100000:
        for kind, token in next_state(lines, offset):
            if kind == 'state_change':
                next_state, offset = token
                break
            elif kind in result_map:
                result_map[kind](kind, token, results)
        iterations += 1

    return results, []


def set_value(kind, token, results):
    results[kind] = token


def append_value(kind, token, results):
    results[kind].append(token)


def parse_time_data(lines, offset):
    for i, line in enumerate(lines[offset:]):
        if i == 0:
            if not TIME_RE.search(line):
                raise Unparsable('Missing datetime.')

            yield 'time', line
        else:
            yield 'state_change', (parse_victim_data, offset + i)

    raise Unparsable('Failed to parse past time.')


def parse_victim_data(lines, offset):
    victim_data = {}
    transition = None
    for line in lines[offset:]:
        offset += 1
        transition = common_transitions(line)
        if transition:
            break

        match = PLAYER_RE.search(line)
        if match:
            key, val = match.groups()
            victim_data[format_key(key)] = val
        else:
            raise Unparsable('Failed parsing at line %s: %s' % (offset, line))

    yield 'victim', victim_data
    yield 'state_change', (transition, offset)


def parse_involved_data(lines, offset):
    player = {}
    transition = None
    for line in lines[offset:]:
        offset += 1
        transition = common_transitions(line)
        if player and line.startswith('Name:'):
            offset -= 1
            transition = parse_involved_data

        if transition:
            break

        match = INVOLVED_RE.search(line)
        if match:
            key, val, killing_blow = match.groups()
            player[format_key(key)] = val
            if killing_blow:
                player['killing_blow'] = True
        else:
            raise Unparsable('Failed parsing at line %s: %s' % (offset, line))

    if player:
        player['killing_blow'] = player.get('killing_blow', False)
        player['damage_done'] = int(player.get('damage_done', 0))
        yield 'involved', player
    yield 'state_change', (transition, offset)


def parse_destroyed_items(lines, offset):
    transition = None
    for line in lines[offset:]:
        offset += 1
        transition = common_transitions(line)
        if transition:
            break

        match = ITEM_RE.search(line)
        if match:
            name, _, quantity, _, location = match.groups()
            yield 'destroyed', {'name': name,
                                'quantity': f_int(quantity) or 1,
                                'location': location}
        else:
            raise Unparsable('Failed parsing at line %s: %s' % (offset, line))

    yield 'state_change', (transition, offset)


def parse_dropped_items(lines, offset):
    for line in lines[offset:]:
        offset += 1
        match = ITEM_RE.search(line)
        if match:
            name, _, quantity, _, location = match.groups()
            yield 'dropped', {'name': name,
                              'quantity': f_int(quantity) or 1,
                              'location': location}
        else:
            raise Unparsable('Failed parsing at line %s: %s' % (offset, line))

    yield 'state_change', (None, offset)


def common_transitions(line):
    if line == 'Involved parties:':
        return parse_involved_data
    elif line == 'Destroyed items:':
        return parse_destroyed_items
    elif line == 'Dropped items:':
        return parse_dropped_items


def format_key(key):
    return key.lower().replace(' ', '_')
