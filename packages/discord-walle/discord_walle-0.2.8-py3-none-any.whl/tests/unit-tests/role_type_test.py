from walle.core import RoleType

import pytest


class Role:
    def __init__(self, name):
        self.name = name

    def __eq__(self, __o):
        return isinstance(__o, Role) and self.name == __o.name


@pytest.mark.parametrize(
    "test_input,search,expected",
    [
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            "archmage",
            Role("archmage"),
        ),
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            "everyone",
            Role("everyone"),
        ),
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            "lama",
            None,
        ),
    ],
)
def test_get_role(test_input, search, expected):
    roles = RoleType(**test_input)
    got = roles.get_role(search)
    assert got == expected


@pytest.mark.parametrize(
    "test_input,expected,new_role",
    [
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            None,
            Role("archmage"),
        ),
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            Role("lama"),
            Role("lama"),
        ),
    ],
)
def test_add_role(test_input, expected, new_role):
    roles = RoleType(**test_input)
    got = roles.add_role(new_role)
    assert got == expected


@pytest.mark.parametrize(
    "test_input,expected,role_name",
    [
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            Role("archmage"),
            "archmage",
        ),
        (
            {
                "key": "id",
                "value": [Role("everyone"), Role("archmage")],
                "name": "dummy-type",
                "mutable": False,
            },
            None,
            "lama",
        ),
    ],
)
def test_remove_role(test_input, expected, role_name):
    roles = RoleType(**test_input)
    got = roles.remove_role(role_name)
    assert got == expected
