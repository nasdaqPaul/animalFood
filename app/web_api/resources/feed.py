from flask import request
from flask_restful import Resource
from marshmallow import Schema, ValidationError
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.models import Feed
from ..schemas import FeedSchema as Schema


class FeedResource(Resource):

    def get(self, sku):
        feed = Feed.query.get(sku)
        if feed is None:
            return "Feed not found", 404
        else:
            schema = Schema.PUT()
            return schema.dump(feed), 200

    def put(self, sku):
        feed = Feed.query.get(sku)
        if feed is None:
            return "Feed not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PUT()
                new_feed = schema.load(data)
            except ValidationError as err:
                return err.messages, 400
            try:
                db.session.delete(feed)
                db.session.add(new_feed)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"sku {new_feed.sku} already exists", 400
            return "put-ed", 200

    def patch(self, sku):
        feed = Feed.query.get(sku)
        if feed is None:
            return "Feed not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PATCH()
                new_feed = schema.load(data)
            except ValidationError as err:
                return err.messages, 400
            for key, value in new_feed.items():
                setattr(feed, key, value)
            try:
                db.session.add(feed)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"sku {new_feed['sku']} already exists.", 400

            return "patched", 200

    def delete(self, sku):
        feed = Feed.query.get(sku)
        if feed is None:
            return "Feed not found", 404
        else:
            db.session.delete(feed)
            db.session.commit()
            return "", 204
