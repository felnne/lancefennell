from pathlib import Path

from flask_frozen import Freezer
from lxml import etree

from lancefennell.app import create_app

app = create_app()
freezer = Freezer(app)

sitemap_path = Path('./exports/sitemap.xml')
output_path = Path('./urls.txt')

namespaces = {
    'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'
}

def _list_redirects():
    redirects = []

    tree = etree.parse(sitemap_path)
    sources = tree.xpath('//ns:url/ns:loc', namespaces=namespaces)
    sources_count = len(sources)
    print(f'{sources_count} sources')
    urls = [str(source.text).replace('https://www.lancefennell.co.uk', '') for source in sources]

    with output_path.open(mode='w') as file:
        for url in urls:
            file.write(f"{url}\n")


if __name__ == '__main__':
    _list_redirects()
