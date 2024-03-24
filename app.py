import random

locations = ["Canada", "United States", "Brazil", "India", "China", "Russia", "Australia", "France", "Germany", "Japan"]

def choose_location(locations_list):
    return random.choice(locations_list).upper()

def display_progress(secret_location, guesses_made):
    display = ""
    for letter in secret_location:
        if letter in guesses_made:
            display += letter + " "
        else:
            display += "_ "
    return display

def process_guess(secret_location, guesses_made, guess):
    guesses_made.add(guess)
    if guess not in secret_location:
        return False
    return True

def play_game():
    secret_location = choose_location(locations)
    guesses_made = set()
    attempts_left = len(secret_location) + 2

    print("Welcome to the Guess the Location game!")
    print(display_progress(secret_location, guesses_made))

    while attempts_left > 0:
        guess = input("Enter your guess (a single letter): ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guesses_made:
            print("You've already guessed that letter.")
            continue

        if process_guess(secret_location, guesses_made, guess):
            print("Correct!")
        else:
            print("Incorrect guess.")
            attempts_left -= 1

        print(display_progress(secret_location, guesses_made))

        if "_" not in display_progress(secret_location, guesses_made):
            print("Congratulations! You've guessed the location:", secret_location)
            break

    if attempts_left == 0:
        print("You ran out of attempts! The location was:", secret_location)

play_game()
