from werkzeug.security import generate_password_hash, check_password_hash

from . import *
from .exceptions import AuthenticationFailure


class User(Document):

    username = StringField()
    pw_hash = StringField()
    vk_id = StringField()

    @classmethod
    def create(cls, username=None, password=None, vk_id=None):
        if username and password:
            return cls(username=username, pw_hash=generate_password_hash(password))

    @classmethod
    def get(cls, username):
        return cls.objects(username=username).first()

    @classmethod
    def login(cls, username, password):
        user = cls.get(username)
        if user and check_password_hash(user.pw_hash, password):
            return user
        raise AuthenticationFailure
