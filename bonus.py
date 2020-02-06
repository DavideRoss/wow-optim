import json
import re

def parse_bonus():
    with open('data/ids.log', 'r') as f:
        raw = f.read()

    bonuses_raw = re.findall(r'bonus_id=\{ (\d+) \}, ilevel_adjust=\{ (-?\d+) \}', raw)
    bonuses = []

    for hit in bonuses_raw:
        bonuses.append({
            'id': hit[0],
            'modifier': int(hit[1])
        })

    with open('data/item_bonuses.json', 'w') as f:
        f.write(json.dumps(bonuses, indent=4))
    