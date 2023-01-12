# from replit import clear
import random
# import random module
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

word = list(random.choice(word_list))
# random set a word from word list
word_length = len(word)
# calculate the word length of the random choice

end_of_game = False
lives = 6

print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

display = []
repeat_guesses = []

for _ in range(word_length):
    display += "_"
# display the empty array based on the word_length


while not end_of_game:
    user_guess = input("Guess a letter:").lower()
    repeat_guesses.append(user_guess)



    if user_guess in word:
        position = word.index(user_guess)
        display[position] = user_guess
        print(display)
        
        if user_guess in repeat_guesses:
            print(f"{' '.join(display)}")
            print(f"You've already guessed with the letter '{user_guess}', pick another letter.")

    else:
        lives -= 1
        print(stages[lives])
        print(f"'{user_guess}' is not in the word, you lost 1 life.")
        print(display)

    if lives == 0:
        end_of_game = True
        print("The man has been hung, you lose.")
        print(f"\nThe word was '{word}'")

