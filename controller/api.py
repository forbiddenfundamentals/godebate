from functools import wraps
from flask import jsonify, Blueprint
from .utils import crossdomain


class ApiBlueprint(Blueprint):

    def route(self, rule, **options):
        super_route = super().route

        def decorator(func):
            return super_route(rule, **options)(crossdomain('*')(self.json_response(func)))
        return decorator

    @staticmethod
    def json_response(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return jsonify({'response': func(*args, **kwargs)})
        return wrapper

api = ApiBlueprint("api", __name__)


@api.route('/authenticate', methods=['POST'])
def authenticate():
    return {'token': "lol"}
