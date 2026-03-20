from __future__ import annotations
from types import NotImplementedType
from typing import Any, Self


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        if User._validate_age(age):
            self._age = age

    @staticmethod
    def _validate_age(age: int) -> bool:
        if not age:
            raise ValueError("Age cannot be blank")

        if not isinstance(age, int):
            raise ValueError(f"Age ({age}) must be an integer")

        if age < 0:
            raise ValueError(f"Invalid age supplied ({age}) - age cannot be < 0")

        return True

    def __str__(self) -> str:
        plural = f"s" if self._age != 1 else f""
        return f"{self.name} is {self._age} year{plural} old"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{name={self.name}, _age={self._age}}}"

    def __eq__(self, other: User) -> bool | NotImplementedType:
        if not isinstance(other, User):
            return NotImplemented

        return self.name == other.name and self._age == other._age

    def __ne__(self, other: User) -> bool | NotImplementedType:
        if not isinstance(other, User):
            return NotImplemented

        return not self == other

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "age": self._age
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(data["name"], data["age"])


if __name__ == "__main__":
    u1 = User("Alice", 1)
    print(u1)

    u2 = User("Angela", 2)
    print(u2)