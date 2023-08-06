import re
from .base import BaseBot

__all__ = [
    "WelcomeBot",
]


class WelcomeBot(BaseBot):
    """Welcome Bot

    The purpose of this welcome bot
    will be a endpoint for any interaction involving
    events and/or actions that are associated with
    welcome to servers/channels/clans/groups/etc

    Parameters
    ----------

    action_config : ActionConfig(Config)
        A typed/defined action config that will
        have a predefined set of supported Primitive OPs

    event_config : EventConfig(Config)
        A typed/defined event config that will
        have a predefined set of supported Primitive OPs

    name : str
        the name of this specific bot

    Usage
    -----

    ```python

    from walle.configs import ActionConfig, EventConfig
    from walle.bot import WelcomeBot

    action_cfg = ActionConfig("welcome-actions")
    event_cfg = EventConfig("welcome-events")
    welcome_bot = WelcomeBot(
        action_config=action_cfg,
        event_cfg=event_cfg,
        name=name,
    )
    ```

    Notes
    -----

        The idea of config classes may change as we develop
            the basic idea seems sounds, but could be an entire rewrite

        We dont have a firm grasp on the scope of each bot, this is
            one direction we can go with it
    """

    def __init__(
        self,
        config,
        guild,
        name="welcome-bot",
    ):
        super().__init__(
            config=config,
            name=name,
        )
        self.guild = guild

    async def greet(self, member):
        if self.guild:
            # from the guild name attempt to get a channel name
            channel = None
            pattern = "(welcome|entry)"
            regex = re.compile(pattern)
            for t in self.guild.text_channels:
                if regex.match(t.name):
                    channel = t
            # from channel attempt to mention a member
            if channel:
                msg = await channel.send(str(self.config))
            else:
                msg = await member.send(str(self.config))
            return msg
        else:
            raise Exception("greeting failure guild not found")
