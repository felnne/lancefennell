import json
from pathlib import Path

from lancefennell.data import data

data_updated = []

assets_endpoint = 'https://assets.lancefennell.co.uk/img'
data_path = Path('src/lancefennell/data.py')

def main():
    for item in data:
        item['index_img_href'] = f"{assets_endpoint}/{item['index_img_href'].split('/')[-1]}"
        item['detail_img_href'] = f"{assets_endpoint}/{item['detail_img_href'].split('/')[-1]}"
        data_updated.append(item)

    with data_path.open(mode='w') as f:
        json.dump(data_updated, f, indent=2)

if __name__ == '__main__':
    main()