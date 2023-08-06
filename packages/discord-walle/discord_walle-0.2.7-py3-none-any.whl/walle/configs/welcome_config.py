from .base import BaseConfig

__all__ = [
    "WelcomeConfig",
]


class WelcomeConfig(BaseConfig):
    """Welcome Config

    This welcome config will consume
    partial data from a member class
    passed in from the discord api

    The data consumed will be set to
    our own types to ensure uniformity
    from each of our class objects and
    solidify certain checks and
    functionality

    Parameters
    ----------

    member : discord.Member
        Member class will be from discord API
            will include pertinent data like username

    name : str
        default is 'welcome-config'
            which is the name of this object
    """

    def __init__(
        self,
        member,
        name="welcome-config",
    ):
        super().__init__(
            member=member,
            name=name,
        )

    def _welcome_message(self):
        __o = self.username
        return f"Welcome to the server, {__o.value}!"

    def __str__(self):
        return self._welcome_message()
