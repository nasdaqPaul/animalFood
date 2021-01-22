from flask import request
from flask_restful import Resource
from marshmallow import ValidationError, Schema

from app import db
from app.main import Animal
from ..schemas import AnimalCollectionSchema as Schema


class AnimalCollectionResource(Resource):
    def get(self):
        return Schema.GET().dump(Animal.query.all(), many=True)

    def post(self):
        try:
            data = request.get_json()
            schema = Schema.POST()
            animal = schema.load(data)
        except ValidationError as err:
            return err.messages, 400
        db.session.add(animal)
        db.session.commit()
        return "posted", 201
