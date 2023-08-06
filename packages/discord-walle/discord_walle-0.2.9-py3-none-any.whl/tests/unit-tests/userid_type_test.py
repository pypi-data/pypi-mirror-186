from walle.core import UserIDType

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "key": "id",
                "value": "1234",
                "name": "dummy-type",
                "mutable": False,
            },
            {
                "key": "id",
                "value": "1234",
                "name": "dummy-type",
                "mutable": False,
            },
        ),
    ],
)
def test_eval(test_input, expected):
    got = UserIDType(**test_input)
    assert got.name == expected["name"]
    assert got.key == expected["key"]
    assert got.value == expected["value"]
    expected = UserIDType(**expected)
    assert got == expected
    assert str(got) == expected.value
