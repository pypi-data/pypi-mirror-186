from .base import PrimitiveType

__all__ = [
    "UserIDType",
]


class UserIDType(PrimitiveType):
    def __init__(
        self,
        key,
        value,
        name="userid-type",
        mutable=False,
    ):

        super().__init__(
            key=key,
            value=value,
            name=name,
            mutable=mutable,
        )

    def __eq__(self, __o):
        return isinstance(__o, type(self)) and (self.value == __o.value)

    def __str__(self):
        return f"{self.value}"
