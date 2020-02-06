import requests
import re
import json

URL = 'https://www.wowhead.com/nyalotha-the-waking-city'

def scrape():
    items = []
    response = requests.get(URL)

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