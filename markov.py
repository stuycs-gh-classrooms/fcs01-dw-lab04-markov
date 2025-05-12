#==================================================
# MARKOV CHAIN LAB
#
# In this lab, you will use a text source of your choosing to
# create a markov model. You will then use that markov model
# to generate new text.
#==================================================
from pprint import pprint
from random import random


#==================================================
# Problem 0: make_word_list(s)
# Input: filename: name of text source
#
# Write a function tha will return a list of words
# contained by the file provided as a parameter.
# Do not remove punctuation or letter cases.

def make_word_list(data_text):
    words = []
    return words

print(('=' * 10) + "Problem 0" + ('=' * 10))
word_list = make_word_list('data/alice.txt')
print(word_list)
# End Problem 0
#==================================================

#==================================================
# Problem 1: make_markov_counts(words)
# Input: words: list of words (output of make_word_list)
#
# Write a function that generates and returns a dictions where:
#   - Each key will be two consecutive words from words.
#   - Each value will be another dictionary:
#     - These keys will be the words that follow the original key.
#     - These values will be the number of times that those words appear.
def make_markov_counts(words):
    d = {}
    return d

print(('=' * 10) + "Problem 1" + ('=' * 10))
markov_model = make_markov_counts(word_list)
print(markov_model)
# End Problem 1
#==================================================

#==================================================
# Problem 2: make_markov_model(counts)
# Input: counts: dictionary formatted as the output of make_markov_counts
#
# Write a function that modifies counts such that:
#   - Each key will will be the same
#   - Each value will be another dictionary:
#     - These keys will be the same.
#     - These values will be the computed probabliities for each word to appear
def make_markov_model(counts):
    return counts

print(('=' * 10) + "Problem 2" + ('=' * 10))
make_markov_model(markov_model)
print(markov_model)
# End Problem 2
#==================================================

#==================================================
# Problem 3: get_next_word(model)
# Input: model: dictionary formatted as one modified by make_markov_model
#
# Write a function that will return a random word chosen from the options
# started key, that respects the probabilities stored in the model.
def get_next_word(model, key):
    word = ''
    return word

print(('=' * 10) + "Problem 3" + ('=' * 10))
key = ''
next_word = get_next_word(markov_model, key)
print('key:', key)
print('next word:', next_word)
# End Problem 3
#==================================================

#==================================================
# Problem 4: generate_text(model, n)
# Input: model: dictionary formatted as one modified by make_markov_model
#        n: integer number of words to generate
# Write a function that will return a string containing n words. All words
# should be consecutive selctions from model using get_next_word
def generate_text(model, n):
    text = ''
    return text

print(('=' * 10) + "Problem 4" + ('=' * 10))
text = generate_text(markov_model, 100)
print(text)
# End Problem 4
#==================================================
