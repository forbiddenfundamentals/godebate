from . import *

from model.resolution import Resolution


def test_create_resolution():
    title = "ЭП уничтожит все произведения искусства, не имеющие унитарной ценности"
    r = Resolution.create(title)
    assert r.title == title
