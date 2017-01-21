from . import *

from model.game import Game
from model.user import User


def test_create_game():
    user = User("lol", "lol")
    name = "IITU Cup 1/2. Room 15"
    r = Game.create(user, name)
    assert r.name == name
