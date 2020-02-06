import requests
import re
import json

URLS = [
    'https://www.wowhead.com/ataldazar',
    'https://www.wowhead.com/operation-mechagon',
    'https://www.wowhead.com/tol-dagor',
    'https://www.wowhead.com/the-underrot',
    'https://www.wowhead.com/kings-rest',
    'https://www.wowhead.com/temple-of-sethraliss',
    'https://www.wowhead.com/freehold',
    'https://www.wowhead.com/waycrest-manor',
    'https://www.wowhead.com/siege-of-boralus',
    'https://www.wowhead.com/shrine-of-the-storm'
]

def scrape():
    items = []

    for url in URLS:
        response = requests.get(url)

        instance = re.findall(r'<title>(.+) - Z', response.text)[0]
        items_raw = re.findall(r"new Listview\(({template: 'item',(.+)data: (.*))}\);", response.text)[0][2].replace('modes', '"modes"')
        items_json = json.loads(items_raw)

        for item in items_json:
            if (item['slot'] == 0):
                continue
                
            items.append({
                'id': item['id'],
                'name': item['name'],
                'slot': item['slot'],
                'instance': instance
            })

    return items