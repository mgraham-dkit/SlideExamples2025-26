from users import User
import json


if __name__ == "__main__":
    u1 = User("Alice", 1)

    # Create JSON string from a User dictionary:
    json_u1 = json.dumps(u1.to_dict(), indent=4)
    print(json_u1)

    obj_dict = json.loads(json_u1)
    u1_fromJSON = User.from_dict(obj_dict)
    print(repr(u1_fromJSON))
