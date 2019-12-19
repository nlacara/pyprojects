#!/bin/python3
"""
Basic NYT spelling bee solver.

TODO:
    - Save word database
    - Better word list?
"""

# We'll use the NLTK words corpus and 
# the brown corpus for our word list
# to generate a list of words.
import nltk
from nltk.corpus import words
from nltk.corpus import brown

# For cli input:
from sys import argv

# For getting letters from user:
def get_center_letter():
    center_letter = input('What is the center letter? ')
    return center_letter


def get_other_letters():
    other_letters = input('What are the other letters? ')
    return other_letters


# Search words for letters:
def letter_check(word):
    has_all_letters = True
    for char in word:
        if char not in ol + cl:
            has_all_letters = False
    return has_all_letters


# Create the wordlist
print("Generating word list.")
words_words = set(word.lower() for word in words.words())
brown_words = set(word.lower() for word in brown.words() if word.isalpha())
wordlist = words_words.intersection(brown_words)
print("Word list generated. Contains {} words.".format(len(wordlist)))


# Get characters from CLI or else direct input:
if len(argv) == 2:
    print('Invalid number of arguments!')
    exit()
elif len(argv) == 3:
    _, cl, ol = argv
    cl = cl.lower()
    ol = ol.lower()
else:
    cl = get_center_letter().lower()
    ol = get_other_letters().lower()


# Check input to make sure it is valid:
if len(cl) != 1 or cl.isalpha() == False:
    print("Invalid input for center letter!")
    exit()
    
if len(ol) != 6 or ol.isalpha() == False:
    print("Invalid input for surrounding letters!")
    exit()

# Find words:
print("Searching for words with '{}' and some".format(cl),
      "combination of the letters '{}'.".format(ol))

words = sorted(list(word for word in wordlist if
         len(word) > 3 
         and cl in word
         and letter_check(word) == True))

print("{} words found!".format(len(words)))
print(words)
