import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, acutual_answer, turns):
    """"Checks answer against guess, returns the number of turns remaining."""
    if user_guess > acutual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < acutual_answer:
        print("Too low.")
        return turns - 1
    else:
        print("You got it!")

def set_difficulty():
    level = input("Choose a difficulty 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    answer = random.randint(1, 100)
    print(f"Welcome to the Number Guessing Game!I'm thinking of a number between 1 and 100. Psst, the correct answer is {answer}.")
    first_question = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = set_difficulty()

    guess = 0
    while guess != answer or turns == 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        check_answer(guess, answer, turns)

game()