from flask import Flask, redirect, url_for, render_template

from lancefennell.data import data


def category_items(category: str):
    items = [item for item in data if item['category'] == category]
    return render_template("items.j2", items=items, category=category)


def create_app():
    app = Flask(__name__)
    app.config['SITE_TITLE'] = 'Lance Fennell'

    @app.route('/')
    def index():
        return redirect(url_for('items', category='studio'))

    @app.route('/<category>')
    def items(category: str) -> str:
        return category_items(category=category)

    @app.route('/items/<slug>')
    def detail(slug: str) -> str:
        item = next((item for item in data if item['slug'] == slug), None)
        return render_template("item.j2", item=item)

    return app
