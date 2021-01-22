from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app import db
from app.main.models import Brand
from ..schemas import BrandCollectionSchema as Schema


class BrandCollectionResource(Resource):

    def get(self):
        return Schema.GET().dump(Brand.query.all(), many=True)

    def post(self):
        try:
            data = request.get_json()
            schema = Schema.POST()
            brand = schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        db.session.add(brand)
        db.session.commit()

        return "Creation success", 201
