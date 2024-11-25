import random


word_list = ['python', 'javascript', 'hangman', 'developer', 'algorithm', 'computer', 'software', 'hardware']


def choose_word():
    return random.choice(word_list)


def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def play_hangman():
    word = choose_word()  
    guessed_letters = []  
    incorrect_guesses = 0  
    max_incorrect_guesses = 6  
    guessed_word = False 
    
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
 
    while incorrect_guesses < max_incorrect_guesses and not guessed_word:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        
        guess = input("Guess a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)

        
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            incorrect_guesses += 1

        
        if all(letter in guessed_letters for letter in word):
            guessed_word = True
    
    
    if guessed_word:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame over! The correct word was: {word}")

if __name__ == "__main__":
    play_hangman()
