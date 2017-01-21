from . import *


class Place(Document):

    name = StringField()

    @classmethod
    def create(cls, name):
        return cls(name=name)
