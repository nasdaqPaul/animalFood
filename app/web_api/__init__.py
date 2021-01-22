from flask import Blueprint
from flask_restful import Api

from .resources.animal import AnimalResource
from .resources.animal_collection import AnimalCollectionResource
from .resources.brand import BrandResource
from .resources.brand_collection import BrandCollectionResource
from .resources.feed import FeedResource
from .resources.feed_collection import FeedCollectionResource

web_api = Blueprint("web_api", __name__, url_prefix='/web-api')


@web_api.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


api = Api(web_api)

api.add_resource(FeedCollectionResource, "/feeds")
api.add_resource(FeedResource, "/feeds/<sku>")

api.add_resource(BrandCollectionResource, '/brands')
api.add_resource(BrandResource, '/brands/<id>')

api.add_resource(AnimalCollectionResource, '/animals')
api.add_resource(AnimalResource, '/animals/<id>')
