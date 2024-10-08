# Lance Fennell

Personal website of Lance Fennell recreated as a static site.

## Generate list of works

- download exports from Square Space to `exports/*.xml`
- remove posts/items for:
  - contact
  - remembrance
  - funeral-attendance
  - funeral
- save URLs from visual tribute to `exports/tribute.txt`
- run: `poetry run python scripts/make_data.py`
- download funeral transcript doc
- save `/sitemap.xml` to `exports/sitemap.xml`

## Download assets

- run: `poetry run python scripts/list_wget.py`
- run `wget -i asset_urls.txt -P ./assets/img`
- delete any `.1` files
- rename any files with `?format=` suffixes

## Upload assets

- create a new CloudFlare R2 bucket (`assets-lancefennell-co-uk`)
- upload contents of `assets/img` to a `img/` prefix (e.g. `foo.png` as `img/foo.png`)
- expose bucket as `assets.lancefennell.co.uk` (e.g. `foo.png` as `https://assets.lancefennell.co.uk/img/foo.png`)
- run: `poetry run python scripts/update_href.py`
- upload funeral transcript doc under a `doc/` prefix

## Developing

- run: `poetry run flask run --app lancefennell.app:create_app --port 9000 --debug`
- run: `poetry run tailwindcss -i src/lancefennell/resources/styles/main.css -o src/lancefennell/static/css/main.css --minify --watch`

## Build site

- run: `poetry run python scripts/make_site.py`
- test site: `poetry run python -m http.server 9000 --directory build`

## Make redirects

- run: `poetry run python scripts/list_redirects.py`
- update `src/lancefennell/resources/cloudflare/_redirects` as needed
