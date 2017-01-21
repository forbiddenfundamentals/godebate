from functools import wraps

from flask import jsonify, Blueprint, request

from model.user import User


class ApiBlueprint(Blueprint):

    def route(self, rule, **options):
        super_route = super().route

        def decorator(func):
            return super_route(rule, **options)(self.json_response(func))
        return decorator

    @staticmethod
    def json_response(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return jsonify({'response': func(*args, **kwargs)})
        return wrapper

api = ApiBlueprint("api", __name__)


@api.route('/register/', methods=['POST'])
def register():
    return {'key': User(username="lol", password="qwerty")}


@api.route('/authenticate/', methods=['POST'])
def authenticate():
    device_id, device_key = request.json['device_id'], request.json['device_key']
    return {'token': Device.generate_token(device_id, device_key)}


@api.route('/me/')
def me_info(device):
    return device.get_info()
