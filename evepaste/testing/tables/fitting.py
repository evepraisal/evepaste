"""
evepaste.testing.tables.fitting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fitting listing table tests

"""
from evepaste import parse_fitting
from evepaste.testing import TableTestGroup


FITTING_TABLE = TableTestGroup(parse_fitting)
FITTING_TABLE.add_test('''High power
5x Heavy Missile Launcher II
Medium power
1x Large Shield Extender II
1x Dread Guristas EM Ward Amplifier
1x Domination 100MN Afterburner
1x Phased Muon Sensor Disruptor I
2x Adaptive Invulnerability Field II
Low power
1x Damage Control II
1x Reactor Control Unit II
3x Ballistic Control System II
Rig Slot
1x Medium Ancillary Current Router I
2x Medium Core Defense Field Extender I
Sub System
1x Tengu Offensive - Accelerated Ejection Bay
1x Tengu Propulsion - Fuel Catalyst
1x Tengu Defensive - Supplemental Screening
1x Tengu Electronics - Dissolution Sequencer
1x Tengu Engineering - Capacitor Regeneration Matrix
Charges
8,718x Caldari Navy Scourge Heavy Missile
1x Targeting Range Dampening Script
Drones
12 Warrior II''', ([
    {'name': 'Heavy Missile Launcher II', 'quantity': 5},
    {'name': 'Large Shield Extender II', 'quantity': 1},
    {'name': 'Dread Guristas EM Ward Amplifier', 'quantity': 1},
    {'name': 'Domination 100MN Afterburner', 'quantity': 1},
    {'name': 'Phased Muon Sensor Disruptor I', 'quantity': 1},
    {'name': 'Adaptive Invulnerability Field II', 'quantity': 2},
    {'name': 'Damage Control II', 'quantity': 1},
    {'name': 'Reactor Control Unit II', 'quantity': 1},
    {'name': 'Ballistic Control System II', 'quantity': 3},
    {'name': 'Medium Ancillary Current Router I', 'quantity': 1},
    {'name': 'Medium Core Defense Field Extender I', 'quantity': 2},
    {'name': 'Caldari Navy Scourge Heavy Missile', 'quantity': 8718},
    {'name': 'Targeting Range Dampening Script', 'quantity': 1},
    {'name': 'Warrior II', 'quantity': 12},
    {'name': '1x Tengu Offensive - Accelerated Ejection Bay', 'quantity': 1},
    {'name': '1x Tengu Propulsion - Fuel Catalyst', 'quantity': 1},
    {'name': '1x Tengu Defensive - Supplemental Screening', 'quantity': 1},
    {'name': '1x Tengu Electronics - Dissolution Sequencer', 'quantity': 1},
    {'name': '1x Tengu Engineering - Capacitor Regeneration Matrix',
     'quantity': 1}], []))
