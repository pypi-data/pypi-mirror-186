from walle.core import UserNameType

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "key": "username",
                "value": "rube",
                "name": "dummy-type",
            },
            {
                "key": "username",
                "value": "rube",
                "name": "dummy-type",
            },
        ),
    ],
)
def test_eval(test_input, expected):
    got = UserNameType(**test_input)
    assert got.name == expected["name"]
    assert got.key == expected["key"]
    assert got.value == expected["value"]
    expected = UserNameType(**expected)
    assert got == expected
    assert str(got) == expected.value
