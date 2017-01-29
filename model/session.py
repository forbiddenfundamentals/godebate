from base64 import b64decode, b64encode

from os import urandom
from datetime import datetime, timedelta

from . import *


class Session(Document):
    token = BinaryField(length=128, default=lambda: urandom(128))
    time_to_die = DateTimeField(default=lambda: datetime.utcnow() + timedelta(days=30))
    user = ReferenceField('User')

    @classmethod
    def create(cls, user):
        session = cls(user=user)
        return session

    @property
    def text_token(self):
        return b64encode(self.token).decode()

    @classmethod
    def find_one_by_token(cls, token):
        session = cls.objects(token=token).first()
        if session and datetime.utcnow() < session.time_to_die:
            return session

    @classmethod
    def find_one_by_text_token(cls, token):
        return cls.find_one_by_token(b64decode(token))
