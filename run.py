import words
import random

def choose_word():
    return random.choice(words.word_list)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        
        guess = input("Enter a letter to guess: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nOut of attempts! The word was:", word)

if __name__ == "__main__":
    hangman()


