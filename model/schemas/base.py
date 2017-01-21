from random import choice

from .. import *
from ..user import User


class Slot(EmbeddedDocument):

    NAME = None
    SHORTCUT = None

    name = StringField()
    shortcut = StringField()
    player = ReferenceField(User)
    blocked = BooleanField(default=False)

    def fill(self, user):
        self.player = user

    def is_filled(self):
        return self.player or self.blocked

    @classmethod
    def create(cls):
        assert cls.NAME is not None, ValueError
        assert cls.SHORTCUT is not None, ValueError
        return cls(name=cls.NAME, shortcut=cls.SHORTCUT)


class Team(EmbeddedDocument):
    NAME = None
    SHORTCUT = None
    SLOT_CLASSES = []

    name = StringField()
    shortcut = StringField()
    slots = MapField(EmbeddedDocumentField(Slot))

    @classmethod
    def create(cls):
        assert cls.NAME is not None, ValueError
        assert cls.SHORTCUT is not None, ValueError
        assert cls.SLOT_CLASSES, ValueError
        team = cls(name=cls.NAME, shortcut=cls.SHORTCUT)
        for slot_class in cls.SLOT_CLASSES:
            slot = slot_class.create()
            team.slots[slot.name] = slot
        return team

    def num_of_filled_slots(self):
        return len(self.get_filled_slots())

    def num_of_free_slots(self):
        return len(self.get_free_slots())

    def get_filled_slots(self):
        return [x for x in self.slots if x.is_filled()]

    def get_free_slots(self):
        return [x for x in self.slots if not x.is_filled()]

    def add_player(self, user, position=None):
        slot = self.slots[position] if position else choice(self.get_free_slots()).fill(user)
        slot.fill(user)
        return slot


class Schema(EmbeddedDocument):
    NAME = None
    TEAM_CLASSES = []
    JUDGE_LIMIT = 5
    CHAIR_LIMIT = 1
    PLAYER_LIMIT = None
    OVERALL_LIMIT = 100

    name = StringField()
    teams = MapField(EmbeddedDocumentField(Team))

    @classmethod
    def create(cls):
        assert cls.NAME is not None, ValueError
        assert cls.TEAM_CLASSES, ValueError
        assert cls.PLAYER_LIMIT is not None
        schema = cls(name=cls.NAME)
        for team_class in cls.TEAM_CLASSES:
            team = team_class.create()
            schema[team.name] = team
        return schema

    def get_free_slots(self):
        return [slot for team in self.teams for slot in team.get_free_slots()]

    def num_of_free_slots(self):
        return len(self.get_free_slots())

    def add_player(self, user, team_name=None, position=None):
        if team_name:
            return self.teams[team_name].add_player(position)
        slot = choice(self.get_free_slots())
        slot.fill(user)
        return slot
