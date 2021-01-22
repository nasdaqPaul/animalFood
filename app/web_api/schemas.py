from marshmallow import Schema, fields, post_load, pre_dump

from app.main import Animal, Brand, Feed


class AnimalCollectionSchema:
    class POST(Schema):
        name = fields.Str(required=True)

        @post_load
        def post_load(self, data, **kwargs):
            return Animal(**data)

    class GET(POST):
        id = fields.Int()


class AnimalSchema:
    class PUT(Schema):
        id = fields.Int(required=True)
        name = fields.Str(required=True)

        @post_load
        def post_load(self, data, **kwargs):
            return Animal(**data)

    class PATCH(Schema):
        id = fields.Int()
        name = fields.Str()


class BrandCollectionSchema:
    class POST(Schema):
        name = fields.Str(required=True)

        @post_load
        def post_load(self, data, **kwargs):
            return Brand(**data)

    class GET(POST):
        id = fields.Int()


class BrandSchema:
    class PUT(Schema):
        id = fields.Int(required=True)
        name = fields.Str(required=True)

        @post_load
        def post_load(self, data, **kwargs):
            return Brand(**data)

    class PATCH(Schema):
        id = fields.Int()
        name = fields.Str()


class FeedSchema:
    class PUT(Schema):
        sku = fields.Str(required=True)
        brand_id = fields.Int(required=True, data_key="brandId", allow_none=True)
        name = fields.Str(required=True)
        animal_id = fields.Int(required=True, data_key="animalId", allow_none=True)
        description = fields.Str(required=True)
        image_url = fields.Str(required=True, data_key="imageUrl")
        purchase_link = fields.Str(required=True, data_key="purchaseLink")
        price_range = fields.Str(required=True, data_key="priceRange")
        min_weight = fields.Int(required=True, data_key="minWeight")
        max_weight = fields.Int(required=True, data_key="maxWeight")
        min_age = fields.Int(required=True, data_key="minAge")
        max_age = fields.Int(required=True, data_key="maxAge")
        allergies = fields.List(fields.Str, required=True, allow_none=True)
        health_issues = fields.List(fields.Str, required=True, data_key="healthIssues", allow_none=True)

        @post_load
        def list_allergies(self, in_data, **kwargs):
            if in_data['allergies'] is not None:
                in_data['allergies'] = ','.join(in_data['allergies'])
            if in_data['health_issues'] is not None:
                in_data['health_issues'] = ','.join(in_data['health_issues'])
            return Feed(**in_data)

        @pre_dump
        def list_to_allergies(self, in_data, **kwargs):
            if in_data.allergies is not None:
                in_data.allergies = in_data.allergies.split(',')
            if in_data.health_issues is not None:
                in_data.health_issues = in_data.health_issues.split(',')
            return in_data

    class PATCH(Schema):
        sku = fields.Str()
        brand_id = fields.Int(data_key="brandId")
        name = fields.Str(required=True)
        animal_id = fields.Int(data_key="animalId")
        description = fields.Str(required=True)
        image_url = fields.Str(data_key="imageUrl")
        purchase_link = fields.Str(data_key="purchaseLink")
        price_range = fields.Str(data_key="priceRange")
        min_weight = fields.Int(data_key="minWeight")
        max_weight = fields.Int(data_key="maxWeight")
        min_age = fields.Int(data_key="minAge")
        max_age = fields.Int(data_key="maxAge")
        allergies = fields.List(fields.Str, required=True)
        health_issues = fields.List(fields.Str, data_key="healthIssues")

        @post_load
        def list_allergies(self, in_data, **kwargs):
            if in_data['allergies'] is not None:
                in_data['allergies'] = ','.join(in_data['allergies'])
            if in_data['health_issues'] is not None:
                in_data['health_issues'] = ','.join(in_data['health_issues'])
            return in_data


class FeedCollectionSchema:
    class PUT(Schema):
        sku = fields.Str(required=True)
        brand_id = fields.Int(required=True, data_key="brandId", allow_none=True)
        name = fields.Str(required=True)
        animal_id = fields.Int(required=True, data_key="animalId", allow_none=True)
        description = fields.Str(required=True)
        image_url = fields.Str(required=True, data_key="imageUrl")
        purchase_link = fields.Str(required=True, data_key="purchaseLink")
        price_range = fields.Str(required=True, data_key="priceRange")
        min_weight = fields.Int(required=True, data_key="minWeight")
        max_weight = fields.Int(required=True, data_key="maxWeight")
        min_age = fields.Int(required=True, data_key="minAge")
        max_age = fields.Int(required=True, data_key="maxAge")
        allergies = fields.List(fields.Str, required=True, allow_none=True)
        health_issues = fields.List(fields.Str, required=True, data_key="healthIssues", allow_none=True)

        @post_load
        def list_allergies(self, in_data, **kwargs):
            if in_data['allergies'] is not None:
                in_data['allergies'] = ','.join(in_data['allergies'])
            if in_data['health_issues'] is not None:
                in_data['health_issues'] = ','.join(in_data['health_issues'])
            return Feed(**in_data)

        @pre_dump
        def list_to_allergies(self, in_data, **kwargs):
            if in_data.allergies is not None:
                in_data.allergies = in_data.allergies.split(',')
            if in_data.health_issues is not None:
                in_data.health_issues = in_data.health_issues.split(',')
            return in_data
