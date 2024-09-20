# Lance Fennell

Personal website of Lance Fennell recreated as a static site.

## Generate list of works

- download exports from Square Space
- remove posts/items for:
  - contact
  - remembrance
  - funeral-attendance
  - funeral
- run: `poetry run python scripts/make_data.py`
- replace `\u2019` with `'` in `src/lancefennell/data.py`
- add `data =` to `src/lancefennell/data.py` to name list

## Download assets

- run: `poetry run python scripts/make_wget.py`
- run `wget -i asset_urls.txt -P ./assets/img`
- delete any `.1` files

## Upload assets

- create a new CloudFlare R2 bucket (`assets-lancefennell-co-uk`)
- upload contents of `assets/img` to a `img/` prefix (e.g. `foo.png` as `img/foo.png`)
- expose bucket as `assets.lancefennell.co.uk` (e.g. `foo.png` as `https://assets.lancefennell.co.uk/img/foo.png`)
- run: `poetry run python scripts/update_href.py`
- add `data =` to `src/lancefennell/data.py` to name list

## Developing

- `poetry run flask run --app lancefennell.app:create_app --port 9000 --debug`
- `poetry run tailwindcss -i src/lancefennell/styles/main.css -o src/lancefennell/static/css/main.css --minify --watch`
