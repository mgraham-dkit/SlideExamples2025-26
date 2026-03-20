from users import User
import json


if __name__ == "__main__":
    u1 = User("Alice", 1)
    u2 = User("Angela", 2)

    # Create JSON string from a User:
    json_u1 = json.dumps(u1, indent=4)