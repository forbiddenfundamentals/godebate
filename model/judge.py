from . import *
from .user import User


class Judge(EmbeddedDocument):
    CHAIR = 'chair'
    WING = 'wing'
    role = StringField(choices=[CHAIR, WING])
    user = ReferenceField(User)
