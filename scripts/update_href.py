import json
from pathlib import Path

from lancefennell.data import data

data_updated = []

assets_endpoint = 'https://assets.lancefennell.co.uk/img'
data_path = Path('src/lancefennell/data.py')

def main():
    for item in data:
        item['index_img_href'] = f"{assets_endpoint}/{item['index_img_href'].split('/')[-1].split('?')[0]}"
        item['detail_img_href'] = f"{assets_endpoint}/{item['detail_img_href'].split('/')[-1].split('?')[0]}"
        data_updated.append(item)
    with data_path.open('w') as f:
        f.write('data = ' + json.dumps(data_updated, indent=2))

if __name__ == '__main__':
    main()