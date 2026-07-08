import random
import art

# Global constants for the respective game mode attempts
EASY_LEVEL_TURNS=10
MEDIUM_LEVEL_TURNS=6
HARD_LEVEL_TURNS=3


# Choose level hard or easy
def set_difficulty():
    """Takes input from the user to select the game mode"""
    mode=str(input("Choose the level of difficulty. Type 'easy', 'medium' or 'hard': "))
    if mode=='easy':
        return EASY_LEVEL_TURNS
    if mode=='medium':
        return MEDIUM_LEVEL_TURNS
    if mode=='hard':
        return HARD_LEVEL_TURNS

def check_answer(guess,actual_number,attempts):
    """Compares the user input from the randomly selected number by the computer"""
    if guess>actual_number:
        print("Too high. \nGuess again.")
        return attempts - 1
    elif guess<actual_number:
        print("Too low. \nGuess again.")
        return attempts - 1
    else:
        print(f"You've got the right answer. It is {actual_number}")
        return

# Game logo
def play_game():
    # Prints the game logo
    print(art.logo)
    # Introduction
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Pick a random number by the computer
    answer=random.randint(1,100)
    # print(f"The number is {answer}.")
    # Takes the total number of attempts by calling the set_difficulty() to the variable "attempts"
    attempts = set_difficulty()

    guess=0        #guess variable is declared

    # Till the time, user is not getting the correct answer the following functionality will repeat
    while guess!=answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=int(input("Make a guess: ")) #asks for the user input to guess

        # Updates the attempts variable after comparing and checking the answer by calling the check_answer()
        attempts=check_answer(guess,answer,attempts)

        # When no attempts are left, the game ends
        if attempts==0:
            print(f"You've run out of guesses and the correct answer is {answer}")
            return

play_game()
