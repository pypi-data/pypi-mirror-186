from .base import PrimitiveType

__all__ = [
    "RoleType",
]


class RoleType(PrimitiveType):
    def __init__(
        self,
        key,
        value,
        name="role-type",
        mutable=True,
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

    # add, remove find
    # find
    def get_role(self, role_name):
        for __o in self.value:
            if __o.name == role_name:
                return __o
        return None

    def add_role(self, new_role):
        if self.get_role(new_role.name):
            return None
        self.value.append(new_role)
        return new_role

    def remove_role(self, role_name):
        __o = self.get_role(role_name)
        if __o:
            self.value.remove(__o)
        return __o
