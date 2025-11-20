import random
import Hangman_word_list

word_list = ["banana", "apple", "pear", "camel", "dog", "cat", "ape"]
display = []
guessed_words = []

#from Hangman_word_list import word_list
chosen_word = random.choice(word_list)
for n in range(0, len(chosen_word)):
    display.append("_")
print(*display)


wl = len(chosen_word)
lives = 6

while wl > 0 or lives == 0:
    guess = input("Guess a letter! ").lower()

    for x in range(len(chosen_word)):
        letter = chosen_word[x]
        if letter == guess:
            display[x] = letter
            wl -= 1
    if guess in guessed_words:
        print("You already guessed that word!")
    guessed_words.append(guess)
    print(*display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("Game Over!")
        if guess in guessed_words:
            print("You already guessed that word!")
        guessed_words.append(guess)
    print(lives)
    print(*guessed_words)
