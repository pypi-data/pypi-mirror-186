from abc import ABCMeta

__all__ = [
    "BaseBot",
]


class BaseBot(metaclass=ABCMeta):
    """Base Bot"""

    def __init__(
        self,
        config,
        name="base-bot",
    ):
        self.config = config
        self.name = name
        if "base" in name:
            with AssertionError as msg:
                print(msg, "Expected new bot class name but got: ", self.name)
