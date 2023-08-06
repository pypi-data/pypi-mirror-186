from abc import ABCMeta, abstractmethod

__all__ = [
    "PrimitiveType",
]


class PrimitiveType(metaclass=ABCMeta):
    """Primitive Base Class"""

    def __init__(
        self,
        key,
        value,
        name="base-type",
        mutable=True,
    ):
        if "base" in name:
            raise AssertionError(f"Expected a specific Type name but got {name}")

        self.key = key
        self.value = value
        self.name = name
        self.mutable = mutable

    def get_value(self):
        """getter for specific type value"""
        return self.value

    def set_value(self, value):
        """setter method for this types value"""
        self.value = value

    def is_mutable(self):
        return self.mutable

    @abstractmethod
    def __eq__(self, __o: object) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
