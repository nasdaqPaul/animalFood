from flask import Blueprint, render_template, jsonify

from app.main.models import Feed

admin = Blueprint('admin', __name__, url_prefix="/admin")


@admin.route('/')
def home():
    return render_template('admin/index.html')


@admin.route('/login')
def login():
    render_template('admin/login.html')


@admin.route('/api')
def api_home():
    all_feeds = Feed.query.all()
    print(all_feeds)
    if all_feeds:
        arr = []
        for obj in all_feeds:
            arr.append(obj.serialize())
        print(arr)
        return jsonify(arr)
    return "haha"
