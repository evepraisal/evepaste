"""
tests.parsers.view_contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~
View Contents list table tests

"""
from evepaste import parse_view_contents
from tests import TableTestGroup


VIEW_CONTENTS_TABLE = TableTestGroup(parse_view_contents)
VIEW_CONTENTS_TABLE.add_test(
    '''
1600mm Reinforced Steel Plates II\tArmor Reinforcer\tLow Slot\t1
100MN Microwarpdrive II\tPropulsion Module\tMedium Slot\t1
Bouncer II\tCombat Drone\tDrone Bay\t1
Bouncer II\tCombat Drone\tDrone Bay\t1
Drone Link Augmentor II\tDrone Control Range Module\tHigh Slot\t1
Large Micro Jump Drive\tMicro Jump Drive\tCargo Hold\t1
Tengu Defensive - Adaptive Shielding\tDefensive Systems\tSubsystem\t1
Large Trimark Armor Pump I\tRig Armor\tRig Slot\t1
Medium Electrochemical Capacitor Booster I\tCapacitor Booster\tMedium Slot\t1
Giant Secure Container\tSecure Cargo Container\t\t1''',
    ([{'group': u'Propulsion Module',
       'location': u'Medium Slot',
       'name': u'100MN Microwarpdrive II',
       'quantity': 1},
      {'group': u'Armor Reinforcer',
       'location': u'Low Slot',
       'name': u'1600mm Reinforced Steel Plates II',
       'quantity': 1},
      {'group': u'Combat Drone',
       'location': u'Drone Bay',
       'name': u'Bouncer II',
       'quantity': 2},
      {'group': u'Drone Control Range Module',
       'location': u'High Slot',
       'name': u'Drone Link Augmentor II',
       'quantity': 1},
      {'group': u'Secure Cargo Container',
       'location': u'',
       'name': u'Giant Secure Container',
       'quantity': 1},
      {'group': u'Micro Jump Drive',
       'location': u'Cargo Hold',
       'name': u'Large Micro Jump Drive',
       'quantity': 1},
      {'group': u'Rig Armor',
       'location': u'Rig Slot',
       'name': u'Large Trimark Armor Pump I',
       'quantity': 1},
      {'group': u'Capacitor Booster',
       'location': u'Medium Slot',
       'name': u'Medium Electrochemical Capacitor Booster I',
       'quantity': 1},
      {'group': u'Defensive Systems',
       'location': u'Subsystem',
       'name': u'Tengu Defensive - Adaptive Shielding',
       'quantity': 1}], []))
VIEW_CONTENTS_TABLE.add_test(
    '''Festival Launcher\tFestival Launcher\t1
Festival Launcher\tFestival Launcher\t1
Hornet EC-300\tElectronic Warfare Drone\t50
Men's 'Esquire' Coat (red/gold)\tOuter\t1
''', ([{'group': u'Festival Launcher',
        'name': u'Festival Launcher',
        'quantity': 2},
       {'group': u'Electronic Warfare Drone',
        'name': u'Hornet EC-300',
        'quantity': 50},
       {'group': u'Outer',
        'name': u"Men's 'Esquire' Coat (red/gold)",
        'quantity': 1}], []))
