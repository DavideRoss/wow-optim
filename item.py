import json
import requests
import re

import util

def download(item, bonus=1637):
    url = 'https://www.wowhead.com/item={}&bonus={}&xml'.format(str(item['id']), str(bonus))
    
    response = requests.get(url)

    with open('items/{}.xml'.format(util.convert_name(item['name'])), 'w') as f:
        f.write(response.text)

    print('"{}" => complete'.format(item['name']))

def extract(item):
    with open('items/{}.xml'.format(util.convert_name(item['name'])), 'r') as f:
        raw = f.read()

    raw_bonus = re.findall(r'<jsonEquip><!\[CDATA\[(.+)\]\]></jsonEquip>', raw)[0]
    bonus_data = json.loads('{' + raw_bonus + '}')

    raw_base = re.findall(r'<json><!\[CDATA\[(.+)\]\]></json>', raw)[0]
    base_data = json.loads('{' + raw_base + '}')

    return {
        'agility': get_key(bonus_data, 'agi'),
        'intellect': get_key(bonus_data, 'int'),
        'strength': get_key(bonus_data, 'str'),
        'stamina': get_key(bonus_data, 'sta'),

        'armor': get_key(bonus_data, 'armor'),
        'slot': get_key(bonus_data, 'slotbak'),
        'durability': get_key(bonus_data, 'dura'),

        'haste': get_key(bonus_data, 'hastertng'),
        'critical': get_key(bonus_data, 'critstrkrtng'),
        'versatility': get_key(bonus_data, 'versatility'),
        'mastery': get_key(bonus_data, 'mastrtng'),

        'class': get_key(base_data, 'classs'),
        'subclass': get_key(base_data, 'subclass')
    }

def get_key(data, key):
    if key in data:
        return data[key]
    else:
        return 0