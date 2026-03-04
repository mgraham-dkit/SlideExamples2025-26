from users import User


def register(users_dict: dict[str, User]) -> str | None:
    valid_user_data = False
    while not valid_user_data:
        new_username = handle_username_entry(users_dict)
        password = handle_password_entry()
        email = input("Enter email address: ")

        try:
            new_user = User(new_username.lower(), password, email.lower())
        except ValueError as e:
            print(f"Registration failed. Error: {e.args[0]}")
            continue

        valid_user_data = True

    if new_user.username() in users_dict:
        print("Username not available. Please try again.")
        return None
    else:
        users_dict[new_user.username()] = new_user
        return new_user.username()

def display_password_requirements():
    print("Password must: ")
    print("\tBe at least 8 characters long")
    print("\tContain at least 1 uppercase")
    print("\tContain at least 1 lowercase")
    print("\tContain at least 1 digit")


def handle_password_entry() -> str:
    matching = False
    while not matching:
        display_password_requirements()
        password = input("Password: ")
        duplicate = input("Enter password again: ")
        if not password == duplicate:
            print("Passwords do not match. Please try again.")
        else:
            matching = True
    return password


def handle_username_entry(users_dict: dict[str, User]) -> str:
    available = False
    while not available:
        new_username = input("Username: ")
        if new_username.lower() in users_dict:
            print(f"Username \"{new_username}\" taken, please enter new username")
        else:
            available = True
    return new_username


def login(users_dict: dict[str, User]) -> str | None:
    username_attempt = input("Enter username: ").lower()
    password = input("Enter password: ")

    if username_attempt in users_dict:
        user = users_dict[username_attempt]
        if user.check_password(password):
            return username_attempt

    print("Login failed - no such username/password")
    return None


def handle_session(users_dict: dict[str, User]) -> None:
    print("*" * 20)
    print("No functionality present")
    print("Session terminating")
    print("*" * 20)


def populate_dataset(users_dict: dict[str, User]) -> None:
    # Create set of users to work with
    u1 = User("michelle", "Passw0rd", "michelle@password")
    u2 = User("hermione", "Wing4rdium", "hermione@email")
    u3 = User("shortyShort", "SuperS3cur3", "short@accepted.com")
    u4 = User("valid_username", "Valid passw0rd", "valid_email@emaildomain.com")
    u5 = User("michelle", "Valid passw0rd", "valid_email@emaildomain.com")
    user_list = [u1, u2, u3, u4, u5]
    # Populate dictionary - do not add users with duplicate usernames
    print()
    print("Now populating user dataset")
    print("-" * 20)
    for user in user_list:
        if user.username() not in users_dict:
            users_dict[user.username()] = user
        else:
            print(f"{user.username()} cannot be added to the system as the username already exists")
            print(f"\tExisting user details: {users_dict[user.username()]}")
            print(f"\tThis user's details: {user}")
    print("-" * 20)


if __name__ == "__main__":
    # Create dictionary for overall storage
    users = {}
    populate_dataset(users)

    print()
    print("Final User dataset:")
    for i, username in enumerate(users, start=1):
        print(f"{i}) {username}")


    logged_in_user = None
    exit_request = False
    while not exit_request:
        if not logged_in_user:
            print("Please choose from the following options:")
            print("1) Register a new user")
            print("2) Login")
            print("Exit to exit the system")

            choice = input("Enter choice: ")
            match(choice.lower()):
                case "1":
                    logged_in_user = register(users)
                case "2":
                    logged_in_user = login(users)
                    pass
                case "exit":
                    exit_request = True
                    logged_in_user = None
                    continue
                case _:
                    print("Please choose one of the specified options")

        if logged_in_user:
            print("You are now logged in!")
            handle_session(users)
            logged_in_user = None
