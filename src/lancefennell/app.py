from pathlib import Path

from flask import Flask, redirect, url_for, render_template

from lancefennell.data import data

def _get_category_items(category: str) -> list[dict]:
    return [item for item in data if item['category'] == category]


def _get_surrounding_items(slug: str):
    previous_item = None
    current_item = None
    next_item = None

    for i, item in enumerate(data):
        if item['slug'] == slug:
            current_item = item
            if i > 0:
                previous_item = data[i - 1]
            if i < len(data) - 1:
                next_item = data[i + 1]
            break

    return previous_item, current_item, next_item


def create_app():
    app = Flask(__name__)
    app.config['SITE_TITLE'] = 'Lance Fennell'
    app.config['FREEZER_DESTINATION'] = Path.cwd() / 'build'

    @app.route('/favicon.ico')
    def favicon():
        return redirect(url_for('static', filename='favicon.ico'))

    @app.route('/')
    def index():
        return redirect(url_for('items', category='studio'))

    @app.route('/<category>/')
    def items(category: str) -> str:
        return render_template("items.j2", items=_get_category_items(category), category=category)

    @app.route('/items/<slug>/')
    def detail(slug: str):
        previous_item, current_item, next_item = _get_surrounding_items(slug)
        return render_template("item.j2", item=current_item, previous=previous_item, next=next_item)

    @app.route('/remembrance/')
    def remembrance():
        return render_template("remembrance.j2")

    @app.route('/visual-tribute/')
    def visual_tribute():
        return render_template("tribute.j2", items=_get_category_items('tribute'))

    return app
