from walle.configs import WelcomeConfig

import pytest


class Role:
    def __init__(self, name):
        self.name = name

    def __eq__(self, __o):
        return isinstance(__o, Role) and self.name == __o.name


class Member:
    def __init__(
        self,
        name,
        roles,
        id=0,
        bot=False,
    ):
        self.name = "rube"
        self._name = name
        self.bot = bot
        self.id = id
        self.__name__ = "Member"
        self.roles = roles


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "name": "dummy-type",
                "roles": [Role("mage")],
            },
            "Welcome to the server, rube!",
        ),
    ],
)
def test_eval(test_input, expected):
    got = Member(**test_input)
    got = WelcomeConfig(got)
    assert str(got) == expected
