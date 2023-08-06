from walle.core import BotType

import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "key": "bot",
                "value": True,
                "name": "bot-type",
            },
            {
                "key": "bot",
                "value": True,
                "name": "bot-type",
            },
        ),
    ],
)
def test_eval(test_input, expected):
    got = BotType(**test_input)
    assert got.name == expected["name"]
    assert got.key == expected["key"]
    assert got.value == expected["value"]
    expected = BotType(**expected)
    assert got == expected
    assert got.value == expected.value
