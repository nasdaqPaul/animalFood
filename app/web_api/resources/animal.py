from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.main.models import Animal
from ..schemas import AnimalSchema as Schema
from ... import db


class AnimalResource(Resource):

    def get(self, id):
        animal = Animal.query.get(id)
        if animal is None:
            return "Animal not found", 404
        else:
            return Schema.PUT().dump(animal)

    def put(self, id):
        animal = Animal.query.get(id)
        if animal is None:
            return "Animal not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PUT()
                new_animal = schema.load(data)
            except ValidationError as err:
                return err.messages, 400
            try:
                db.session.delete(animal)
                db.session.add(new_animal)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"ID {new_animal.id} already exists.", 400
            return "put-ed", 200

    def patch(self, id):
        animal = Animal.query.get(id)
        if animal is None:
            return "Animal not found", 404
        else:
            try:
                data = request.get_json()
                schema = Schema.PATCH()
                new_animal = schema.load(data)
            except ValidationError as err:
                return err.messages, 400
            for key, value in new_animal.items():
                setattr(animal, key, value)
            try:
                db.session.add(animal)
                db.session.commit()
            except IntegrityError as err:
                db.session.rollback()
                return f"ID {new_animal['id']} already exists.", 400
            return "patched", 200

    def delete(self, id):
        animal = Animal.query.get(id)
        if animal is None:
            return "Animal not found", 404
        else:
            db.session.delete(animal)
            db.session.commit()
            return "deleted", 200
