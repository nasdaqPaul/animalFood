from flask import Blueprint, render_template, request
from .models import Animal, Brand, Feed
main = Blueprint("main", __name__)


@main.route('/')
def home():
    animals = Animal.query.all()
    if request.args:
        animal_id = request.args.get('animal')
        age = request.args.get('age')
        weight = request.args.get('weight')

        feeds = Feed.query.filter(Feed.animal_id == animal_id, Feed.min_age <= int(float(age)), Feed.max_age >= int(float(weight))).all()
        return render_template("main/index.html", animals=animals, feeds=feeds)
    return render_template("main/index.html", animals=animals)


@main.route('/about')
def about():
    return render_template('main/about.html')
