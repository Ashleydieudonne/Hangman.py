import random
from words import words
import string

def getWords(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = getWords(words)
    word_letters = set(word) 
    used_letters = set()

    while len(word_letters) > 0:
     print("You have used: ", ' '.join(used_letters))
     word_list = [letter if letter in used_letters  else '_' for letter in word]
     print('Current word: ', ' '.join(word_list))
     user_letter = input("Guess a letter: ")
     if user_letter.isalpha():
        if user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
     elif user_letter in used_letters:
        print("You Have already used this letter")
     else:
        print("Character is invalid")
        
hangman() 
