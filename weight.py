import json

with open('weights/cleave.json', 'r') as f:
    CLEAVE = json.loads(f.read())

with open('weights/single-target.json', 'r') as f:
    SINGLE_TARGET = json.loads(f.read())

def weight_item(item, weights=SINGLE_TARGET):
    val = 0

    if 'crit' in item:
        val += item['crit'] * weights['crit']

    if 'haste' in item:
        val += item['haste'] * weights['haste']

    if 'mastery' in item:
        val += item['mastery'] * weights['mastery']

    if 'versatility' in item:
        val += item['versatility'] * weights['versatility']

    if 'strength' in item:
        val += item['strength'] * weights['strength']

    return val