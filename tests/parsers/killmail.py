"""
tests.parsers.killmail
~~~~~~~~~~~~~~~~~~~~~~
Killmail table tests

"""
from evepaste import parse_killmail, Unparsable
from tests import TableTestGroup


KILLMAIL_TABLE = TableTestGroup(parse_killmail)
KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim
Corp: Victim's Corp Name
Alliance: Victim's Alliance Name
Faction: Unknown
Destroyed: Scimitar
System: Jita
Security: 0.9
Damage Taken: 14194

Involved parties:

Name: Ganker Name (laid the final blow)
Security: -1.00
Corp: Ganker Corp
Alliance: Ganker Alliance
Faction: Unknown
Ship: Apocalypse Navy Issue
Weapon: Mega Pulse Laser II
Damage Done: 14194

Name: Ganker Name2
Security: -10.00
Corp: Ganker Corp
Alliance: Ganker Alliance
Faction: Unknown
Ship: Rifter
Weapon: Some tiny little gun
Damage Done: 0

Destroyed items:

Medium Armor Maintenance Bot I, Qty: 3 (Drone Bay)
Power Diagnostic System II (Cargo)

Dropped items:

Warrior II (Drone Bay)''', ({
    'destroyed': [{'location': 'Drone Bay',
                   'name': 'Medium Armor Maintenance Bot I',
                   'quantity': 3},
                  {'location': 'Cargo',
                   'name': 'Power Diagnostic System II',
                   'quantity': 1}],
    'dropped': [{'location': 'Drone Bay',
                 'name': 'Warrior II',
                 'quantity': 1}],
    'involved': [{'alliance': 'Ganker Alliance',
                  'corp': 'Ganker Corp',
                  'damage_done': 14194,
                  'faction': 'Unknown',
                  'name': 'Ganker Name',
                  'security': '-1.00',
                  'ship': 'Apocalypse Navy Issue',
                  'weapon': 'Mega Pulse Laser II',
                  'killing_blow': True},
                 {'alliance': 'Ganker Alliance',
                  'corp': 'Ganker Corp',
                  'damage_done': 0,
                  'faction': 'Unknown',
                  'name': 'Ganker Name2',
                  'security': '-10.00',
                  'ship': 'Rifter',
                  'weapon': 'Some tiny little gun',
                  'killing_blow': False}],
    'time': '2013.06.15 17:28:00',
    'victim': {'alliance': "Victim's Alliance Name",
               'corp': "Victim's Corp Name",
               'damage_taken': '14194',
               'destroyed': 'Scimitar',
               'faction': 'Unknown',
               'security': '0.9',
               'system': 'Jita',
               'victim': 'Some poor victim'}}, []))

KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim
Corp: Victim's Corp Name
Damage Taken''', Unparsable)

KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim
Corp: Victim's Corp Name''', ({'destroyed': [], 'dropped': [], 'involved': [],
                               'victim': {'corp': "Victim's Corp Name",
                                          'victim': 'Some poor victim'},
                               'time': '2013.06.15 17:28:00'}, []))
KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim

Involved parties:

Name: Ganker Name (laid the final blow)
Security: -1.00
Some garbage data here''', Unparsable)

KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim

Destroyed items:

Medium Armor Maintenance Bot I, Qty: 3 (Drone Bay)
#$%^&*(''', Unparsable)

KILLMAIL_TABLE.add_test(
    '''2013.06.15 17:28:00

Victim: Some poor victim

Dropped items:

Medium Armor Maintenance Bot I, Qty: 3 (Drone Bay)
#$%^&*(''', Unparsable)
