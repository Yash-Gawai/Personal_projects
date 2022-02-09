import random
import string
from word_list import words # From the word_list.py file import whatever is stored in variable "words"

def valid_words(words):
    word = random.choice(words) # Randomly choose a word from the list
    while "-" in word or " " in word:  # To skip words with spaces or hyphens in them
        word = random.choice(words)
    return word.lower()  # To force return as upper or lower case as desired

def hangman():
    word=valid_words(words)
    word_letters=set(word) # Set of letters in the word
    alphabet=set(string.ascii_lowercase) # Set of all alphabets available. lowercase as return in valid_words is also lower case
    used_letters=set()  # Set of what has been guessed
    life = 0
    if len(word) < 5 :
        print("Easy word")
        life = 3
    if len(word) in range(5,8):
        print("Medium word")
        life = 5
    if len(word) in range(8,10):
        print("Hard word")
        life = 8
    
    # User inputs
    while len(word_letters) > 0 and life > 0:

        print("You have" , life, "lives. Already used letters are: ", " ".join(used_letters)) # To print already used letters

        # To display what the current word looks like
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word is " , " ".join(word_list))


        user_letter=input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters: # To check if its a valid alphabet that has not been entered before
            used_letters.add(user_letter) # Adds it to the set used letters
            if user_letter in word_letters: # Checks the word for used letters
                print("Correct letter used!!!")
                word_letters.remove(user_letter) # Removes the user letter from the word
            else:
                life = life -1 # Takes away a life if guess is wrong
                print("Wrong guess!")
        
        elif user_letter in used_letters:
            print("Already used, enter another letter.")
        
        else:
            print("Not a valid input for letter.")
        
        
    #  Here the len(word_letters) == 0 or life ==0
    
    print(f"The word is {word}")


hangman()