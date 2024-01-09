import random
import hangman_words
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print(f"Hint, word is {chosen_word}")
# Create blanks
display = ['_' for i in range(word_length)]
guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    if guess in guesses:
        print("You have already guessed that! You have lost a life. Please try again.")
        lives -= 1
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lost")
            print(f"Answer was: {chosen_word}")
            end_of_game = True
        continue
    guesses += guess
    # Check guessed letter and replace display
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lost.")
        print(f"Answer was: {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"You guessed: {guess}")
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
