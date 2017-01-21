from . import *

import pytest

from werkzeug.security import check_password_hash, generate_password_hash

from model.user import User
from model.exceptions import AuthenticationFailure


@pytest.fixture(scope="function", params=[
    ("underbird", "123"),
    ("rimus", "lol")
])
def user_data(request):
    username, password = request.param
    user_ = User.create(username, password)
    user_.save()
    yield user_, username, password


def test_create_user(user_data):
    user, username, password = user_data

    assert user.username == username
    assert check_password_hash(user.pw_hash, password)


def test_authentication(user_data):
    user, username, password = user_data

    assert User.login(username, password).pk == user.pk

    with pytest.raises(AuthenticationFailure):
        User.login(username, password + "1")

    with pytest.raises(AuthenticationFailure):
        User.login(username + "1", password)
