from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app import db
from app.main import Feed
from ..schemas import FeedCollectionSchema as Schema


class FeedCollectionResource(Resource):

    def get(self):
        schema = Schema.PUT()
        feeds = Feed.query.all()
        return schema.dump(feeds, many=True)

    def put(self):
        try:
            data = request.get_json()
            schema = Schema.PUT()
            new_feed = schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        try:
            db.session.add(new_feed)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
            return f"sku {new_feed.sku} already exists.", 400
        return "put-ed", 200
