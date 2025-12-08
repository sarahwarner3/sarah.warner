#-------HANGMAN GAME-------#

import random
import hangman_words

lives = 6

import hangman_art
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You have {lives}/6 lives remaining.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}. Choose another letter.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(F"{guess} is not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"You lose. The word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("Congrats, you win.")

    print(hangman_art.stages[lives])
