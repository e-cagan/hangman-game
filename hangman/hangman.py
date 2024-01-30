import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. You've used these letters: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                for i in range(len(word)):
                    if word[i] == user_letter:
                        word_list[i] = user_letter
                if word_list == list(word):
                    break
            else:
                lives -= 1

        elif user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"Congrats! You've guessed the correct word which is {word}")

hangman()