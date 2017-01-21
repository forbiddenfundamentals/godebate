from . import *


class Resolution(Document):

    title = StringField()

    @classmethod
    def create(cls, title):
        return cls(title=title)
