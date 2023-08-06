from .base import PrimitiveType

__all__ = [
    "BotType",
]


class BotType(PrimitiveType):
    def __init__(
        self,
        key,
        value,
        name="bot-type",
        mutable=False,
        isbot=False,
    ):

        super().__init__(
            key=key,
            value=value,
            name=name,
            mutable=mutable,
        )

        self.isbot = isbot

    def __eq__(self, __o):
        return isinstance(__o, type(self)) and (self.value == __o.value)

    def __str__(self):
        return f"{self.value}"

    def is_bot(self):
        return self.isbot
