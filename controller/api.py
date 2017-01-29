from functools import wraps
from flask import jsonify, Blueprint, request
from .utils import crossdomain, authentication_required

from model.user import User
from model.exceptions import AuthenticationFailure, GodebateException


class ApiBlueprint(Blueprint):

    def route(self, rule, **options):
        super_route = super().route

        def decorator(func):
            return super_route(rule, **options)(crossdomain('*', headers=['content-type'])(self.json_response(func)))
        return decorator

    def errorhandler(self, code_or_exception, code=500):
        super_errorhandler = super().errorhandler

        def decorator(func):
            return super_errorhandler(code_or_exception)(self.with_code(code)(crossdomain('*')(self.json_response(func))))
        return decorator

    @staticmethod
    def json_response(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return jsonify({'response': func(*args, **kwargs)})
        return wrapper

    @staticmethod
    def with_code(code):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs), code
            return wrapper
        return decorator

api = ApiBlueprint("api", __name__)


@api.route('/register', methods=['POST'])
def register():

    return {'token': User.create(request.json['username'],
                                 request.json['password']).save().make_session().save().text_token}


@api.route('/authenticate', methods=['POST', 'OPTIONS'])
def authenticate():
    return {'token': User.login(request.json['username'], request.json['password']).save().text_token}


@api.errorhandler(AuthenticationFailure, 403)
def any_exception(e):
    return {'error_name': type(e).__name__}


@api.errorhandler(GodebateException, 500)
def any_exception(e):
    return {'error_name': type(e).__name__}