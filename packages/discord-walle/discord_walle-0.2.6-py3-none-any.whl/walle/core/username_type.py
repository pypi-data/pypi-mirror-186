from .base import PrimitiveType

__all__ = [
    "UserNameType",
]


class UserNameType(PrimitiveType):
    def __init__(
        self,
        key,
        value,
        name="username-type",
    ):

        super().__init__(
            key=key,
            value=value,
            name=name,
        )

    def __eq__(self, __o):
        return isinstance(__o, type(self)) and (self.value == __o.value)

    def __str__(self) -> str:
        return f"{self.value}"
