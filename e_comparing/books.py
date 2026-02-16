from __future__ import annotations
from functools import total_ordering
from types import NotImplementedType


@total_ordering
class Book:
    def __init__(self, title: str, author:str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"\'{self.title}\' by {self.author}"

    def __eq__(self, other: Book) -> NotImplementedType | bool:
        if not isinstance(other, Book):
            return NotImplemented
        if self.author != other.author:
            return False
        if self.title != other.title:
            return False

        return True

    def __ne__(self, other: Book) -> NotImplementedType | bool:
        if not isinstance(other, Book):
            return NotImplemented
        return not self == other

    def __lt__(self, other: Book) -> NotImplementedType | bool:
        if not isinstance(other, Book):
            return NotImplemented
        else:
            return self.title < other.title
