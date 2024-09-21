from pathlib import Path
from shutil import copyfile

from flask_frozen import Freezer

from lancefennell.app import create_app

app = create_app()
freezer = Freezer(app)

sitemap_path = Path('./exports/sitemap.xml')
redirects_path = Path('./src/lancefennell/resources/cloudflare/_redirects')

if __name__ == '__main__':
    freezer.freeze()
    copyfile(redirects_path, app.config['FREEZER_DESTINATION'] / '_redirects')
