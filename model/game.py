from datetime import datetime

from . import *
from .user import User
from .judge import Judge

from .schemas import Schema, BPFSchema


class Game(Document):

    author = ReferenceField(User, required=True)
    name = StringField(required=True)
    schema = EmbeddedDocumentField(Schema, required=True)
    date_created = DateTimeField(default=lambda: datetime.utcnow())
    date_planned = DateTimeField(required=True)
    place = StringField()  # TODO replace with Place reference field if necessary
    resolution = StringField()  # TODO the same here

    @classmethod
    def create(cls, author, name):
        game = cls(name=name, author=author)
        game.schema = BPFSchema.create()
        return game

    wait_list = ListField(User)

    judges = EmbeddedDocumentListField(Judge)
    watchers = ListField(ReferenceField(User))
