import json

import mythics
import nyalotha
import item
import util
import weight
import bonus

items = []

# items += mythics.scrape()
# items += nyalotha.scrape()

# with open('data/items_simple.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(items, indent=4))

# with open('data/items_simple.json', 'r') as f:
#     items = json.loads(f.read())

# for i in items:
#     item.download(i)

# item.extract(items[1])

# items_complex = []

# TODO: fix bonus number for ny'alotha/mechagon items

# for i in items:
#     item_data = item.extract(i)
#     item_complete = { **i, **item_data }
#     items_complex.append(item_complete)

# with open('data/items_complex.json', 'w') as f:
#     f.write(json.dumps(items_complex, indent=4))

with open('data/items_complex.json', 'r') as f:
    items = json.loads(f.read())

weight_data = {}

INCLUDE_SUBCLASSES = [0, 4, 8]

# TODO: fix one-hand mace slot
# TODO: compare all two-hands weapon togheter

# for i in items:
#     if i['subclass'] not in INCLUDE_SUBCLASSES:
#         continue

#     w = weight.weight_item(i)

#     if i['slot'] not in weight_data:
#         weight_data[i['slot']] = []

#     weight_data[i['slot']].append({
#         'item': i['name'],
#         'link': 'https://www.wowhead.com/item={}&bonus=1637'.format(i['id']),
#         'instance': i['instance'],
#         'weight': w
#     })

# for slot in weight_data:
#     print('{} => {}'.format(slot, len(weight_data[slot])))
#     weight_data[slot].sort(key=lambda i: i['weight'], reverse=True)

# with open('data/weight_data.json', 'w') as f:
#     f.write(json.dumps(weight_data, indent=4))

bonus.parse_bonus()