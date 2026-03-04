from functools import total_ordering
from types import NotImplementedType


@total_ordering
class User:
    def __init__(self, username: str, password: str, email:str):
        if not User.__validate_username(username):
            raise ValueError("Supplied username is invalid")
        self._username = username

        if not User.__validate_password(password):
            raise ValueError("Password does not meet requirements - Supplied password is invalid")
        self.__password = password

        if not User.__validate_email(email):
            raise ValueError("Supplied email is invalid")
        self._email = email

    # Getter methods so we can see the encapsulated information outside this class
    # No getter for password as it's sensitive information!
    def username(self) -> str:
        return self._username

    def email(self) -> str:
        return self._email

    def check_password(self, other_pass: str) -> bool:
        return other_pass == self.__password

    # Validator methods
    @staticmethod
    def __validate_username(username: str) -> bool:
        if username is None:
            return False

        if len(username.strip()) < 8:
            return False

        return True

    @staticmethod
    def __validate_password(password: str) -> bool:
        if password is None:
            return False

        if len(password) < 8:
            return False

        # Check each character in password for uppercase status - true if there is any appearance of uppercase
        upper_check = any((c.isupper() for c in password))
        if not upper_check:
            print("No uppercase letter included")
            return False

        # Check each character in password for lowercase status - true if there is any appearance of lowercase
        lower_check = any((c.islower() for c in password))
        if not lower_check:
            print("No lowercase letter included")
            return False

        # Check each character in password for digit status - true if there is any digit appears
        digit_check = any((c.isdigit() for c in password))
        if not digit_check:
            print("No digit included")
            return False

        return True

    @staticmethod
    def __validate_email(email: str) -> bool:
        if email is None:
            return False

        if "@" not in email:
            return False

        return True

    # Text representation
    def __str__(self) -> str:
        return f"Username: {self._username} - {self._email}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[_username={self._username}, __password=\"********\", _email={self._email}]"

    # Equality comparison
    def __eq__(self, other: object) -> bool | NotImplementedType:
        # Confirm other is the right type, return NotImplemented if not
        # If we don't know how to compare to other's type, let other object try
        if not isinstance(other, User):
            return NotImplemented

        # username is identifying attribute
        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, User):
            return NotImplemented

        # Use eq logic to check for equality; flip result to get not equal
        return not self == other

    def __hash__(self) -> int:
        return hash(self._username)

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, User):
            return NotImplemented

        return self._username < other._username
