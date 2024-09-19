# Lance Fennell

Personal website of Lance Fennell recreated as a static site.

- download exports from Square Space
- remove posts/items for:
  - contact
  - remembrance
  - funeral-attendance
  - funeral
- run: `poetry run python scripts make_data.py`
- replace `\u2019` with `'` in `src/lancefennell/data.py`
- add `data =` to `src/lancefennell/data.py` to name list
