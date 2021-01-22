from flask import request
from flask_restful import Resource
from marshmallow import ValidationError, Schema
from sqlalchemy.exc import IntegrityError

from app.main.models import Brand
from ..schemas import BrandSchema as Schema
from ... import db


class BrandResource(Resource):
    def get(self, id):
        brand = Brand.query.get(id)
        if brand is None:
            return "Brand not found", 404
        else:
            schema = Schema.PUT()
            return schema.dump(brand)

    def put(self, id):
        brand = Brand.query.get(id)
        if brand is None:
            return "Brand not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PUT()
                new_brand = schema.load(data)
            except ValidationError as err:
                return err.messages, 400
            try:
                db.session.delete(brand)
                db.session.add(new_brand)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"ID {new_brand.id} already exists.", 400
            return "put-ed", 200

    def patch(self, id):
        brand = Brand.query.get(id)
        if brand is None:
            return "Brand not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PATCH()
                new_brand = schema.load(data)
            except ValidationError as err:
                return err.messages, 404
            for key, value in new_brand.items():
                setattr(brand, key, value)
            try:
                db.session.add(brand)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"ID {new_brand['id']} already exists for another record", 400
            return "patched", 200

    def delete(self, id):
        brand = Brand.query.get(id)
        if brand is None:
            return "Brand not found", 404
        else:
            db.session.delete(brand)
            db.session.commit()

            return "deleted", 200
