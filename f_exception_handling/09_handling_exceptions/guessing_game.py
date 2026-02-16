from random import randint

def guessing_game(min_limit: int, max_limit: int, guess_limit: int) -> bool:
    # Set up game values
    value = randint(min_limit, max_limit)
    guesses = []
    win_status = False

    # While there are guesses left and the game is still in play
    while len(guesses) < guess_limit and not win_status:
        try:
            guess = int(input(f"Please guess a number between {min_limit} and {max_limit}: "))
        except ValueError as e:
            print(f"An error occurred: {e.__class__.__name__}")
            print("Please enter a number using only digits")
            print()
            continue

        # Save the guess
        guesses.append(guess)

        # Check if the guess is correct and update the user accordingly
        if guess == value:
            print("Congratulations!")
            win_status = True
        elif guess < value:
            print("Too low")
        else:
            print("Too high!")

    # Display final result information and return result
    print(f"The number was {value}")
    print(f"You guessed: {guesses}")
    return win_status


keep_playing = True
max_guesses = 5
min_value = 1
max_value = 100

num_wins = 0
num_attempts = 0

while keep_playing:
    choice = input("Do you want to play a guessing game? (Y/N)\n")
    match choice.lower():
        case "y":
            print("Great, let's go!")
        case "n":
            print("Ok, see you later")
            keep_playing = False
            continue
        case _:
            print("Please choose Y or N")
            continue

    num_attempts += 1
    game_won = guessing_game(min_value, max_value, max_guesses)
    if game_won:
        num_wins += 1

print(f"You won {num_wins} games out of {num_attempts} attempts")