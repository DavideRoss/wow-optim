import re

def convert_name(name):
    return re.sub(r'[\' ]+', '-', name.lower())

SLOTS = [
    'ammo',
    'head',
    'neck',
    'shoulder',
    'shirt',
    'chest',
    'waist',
    'legs',
    'feet',
    'wrist',
    'hands',
    'finger 1',
    'finger 2',
    'trinket 1',
    'trinket 2',
    'back',
    'main hand',
    'off hand',
    'ranged',
    'tabard'
]

CLASSES = [
    '??',
    '??',
    'Weapon',
    '??',
    'Armor',
]

# If subclass < 0 counts as 0
# -2 finger
# -4 trinket
# -5 held in off hand
# -6 back
SUBCLASSES = [
    'Miscellaneous',
    'Cloth',
    'Leather',
    'Mail',
    'Plate',
    'Cosmetic',         # 5
    'Polearm/Shield',
    'One-hand Sword',
    'Two-hand Sword',
    'Warglaives',
    'Staff',            # 10
    '??',
    '??',
    'Fist Weapon',
    '??',
    'Dagger',           # 15
    '??',
    '??',
    'Crossbow',
    'Wand'
]