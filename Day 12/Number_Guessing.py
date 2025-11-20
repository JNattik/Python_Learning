#1. Random number has to be established
#2. Text comes
#3. Function, which looks, whether guess = number
#4. Variable "guesses" must be created --> when one guess is wrong this numbers goes down
#5. If statement, depending on which difficulty, has to be created

import random

number = -1
guesses_left = -1
guess = -1

#def number_comparison():
    #number = -1
    #guesses_left = -1
    #guess = -1

print(f"Welcome to the Number Guessing Game!I'm thinking of a number between 1 and 100.Psst, the correct answer is {number}.")
first_question = input("Choose a difficulty. Type 'easy' or 'hard': ")
if first_question == "easy":
    guesses_left = 10
elif first_question == "hard":
    guesses_left = 5
number = random.randint(1, 100)
while guesses_left > 0 or guess != number:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("You guessed the right number, you win!")
        exit()
    elif number < guess:
        guesses_left -= 1
        print(f"Too high, guess again. You have {guesses_left} guesses left.")
    elif number > guess:
        guesses_left -= 1
        print(f"Too low, guess again. You have {guesses_left} guesses left.")