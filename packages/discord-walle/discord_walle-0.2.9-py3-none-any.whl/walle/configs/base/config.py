from abc import ABCMeta, abstractmethod
from walle import core
from . import constants

__all__ = [
    "BaseConfig",
]


class BaseConfig(metaclass=ABCMeta):
    """Base Config"""

    def __init__(
        self,
        member,
        name="base-config",
    ):

        if "base" in name:
            raise AssertionError(
                f"Expected a valid name, but received base class name: {name}"
            )
        self.name = name

        self._parse_types(member)

    def _parse_types(self, member):
        """config types builder"""
        params = constants.constants
        # iterate over all params we set in our json
        # for every attribute we want from Member
        for k, named_attr in params[self.name].items():

            # iterate over all type objects within core
            for t in core.__all__:

                # match upper of type object to our config attribute
                if t[:-4].upper() == k:

                    # get our type object
                    __o = getattr(core, t)
                    # get named attribute from Member
                    v = getattr(member, named_attr)

                    # if either object is none then fail
                    if v is None or __o is None:
                        raise ValueError(
                            "Expected to find {named_attr}, but it does not exist!"
                        )
                    # create our in-house type object
                    __o = __o(named_attr, v)
                    # setting that object to the named attribute
                    # e.g, self.username = UserNameType("username", Member.username)
                    setattr(self, k.lower(), __o)

    def get_type(self, key):
        """getter method for snagging typed values"""
        return getattr(self, key)

    def set_type(self, __o, value):
        """setter to change a mutable attribute"""
        if __o.is_mutable:
            setattr(self, __o.key, value)
        else:
            print(
                f"Config got a request to change a immutable type {type.key} with {value}. It is not allowed"
            )

    @abstractmethod
    def __str__(self):
        """to string method"""
        pass
