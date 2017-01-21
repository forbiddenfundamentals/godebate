from . import *

from model.place import Place


def test_create_place():
    name = 'Кафе "Принцесса" (Гоголя-Тулебаева)'
    r = Place.create(name)
    assert r.name == name
