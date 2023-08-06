from walle.core import PrimitiveType

import pytest


class DummyType(PrimitiveType):
    def __init__(
        self,
        key,
        value,
        name,
    ):
        super().__init__(
            key,
            value,
            name,
        )

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, type(self)) and (__o.key == self.key)

    def __str__(self):
        return f"{self.name}"


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
    got = DummyType(**test_input)
    assert got.name == expected["name"]
    assert got.key == expected["key"]
    assert got.value == expected["value"]
    expected = DummyType(**expected)
    assert got == expected
    assert str(got) == expected.name
