import json
from pathlib import Path
from lxml import etree

exports = ['studio', 'paintings']
output = Path('src/lancefennell/data.py')

namespaces = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/'
}

def process_file(path: Path, link_prefix: str) -> list[dict]:
    print('Processing', path.resolve())
    results = []
    tree = etree.parse(path)
    root = tree.getroot()

    items = root.xpath('//channel/item')
    items_count = len(items)
    print(f'{items_count} items')
    for i in range(0, items_count, 2):
        print(f'Processing items {i} and {i + 1} / {items_count} from {path.resolve()}')

        # Odd-indexed item (post containing title, slug and image)
        odd_item = items[i]
        title = odd_item.find('title').text
        link = str(odd_item.find('link').text).replace(f"/{link_prefix}/", '')

        # img element is buried in cdata
        content_encoded = odd_item.find('content:encoded', namespaces).text
        img_tree = etree.HTML(content_encoded)
        img_tag = img_tree.xpath('//img')
        img_src = img_tag[0].get('src')

        # Even-indexed item (attachment, containing square image)
        even_item = items[i + 1]
        attachment_url = str(even_item.find('wp:attachment_url', namespaces).text).replace('http://', 'https://')

        results.append({
            'category': link_prefix,
            'slug': link,
            'title': title,
            'detail_img_href': img_src,
            'index_img_href': attachment_url
        })
    return results

def main():
    items = []
    for export in exports:
        items.extend(process_file(path=Path(f"data/{export}.xml"), link_prefix=export))
    with output.open('w') as f:
        json.dump(items, f, indent=2)

if __name__ == '__main__':
    main()
