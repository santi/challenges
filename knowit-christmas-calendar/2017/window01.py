
import os

n_gram_anagram = 'aeteesasrsssstaesersrrsse'

def load_words(filename):
    words = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        for line in f.readlines():
            words.append(line.strip().lower())
    return words
words = load_words('input01.txt')

def get_words_with_length(words, length):
    filtered_words = []
    for word in words:
        if len(word) == length:
            filtered_words.append(word)
    return filtered_words
words_with_nine_letters = get_words_with_length(words, 9)
print(len(words_with_nine_letters))

def letter_count(word):
    letters = {}
    for letter in word:
        if letters.get(letter):
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
letters_used = letter_count(n_gram_anagram).keys()

print(letters_used)


def get_words_with_letters(words, letters):
    filtered_words = []
    for word in words:
        invalid = False
        for letter in word:
            if letter not in letters:
                invalid = True
                break
        for letter in letters:
            if letter not in word:
                invalid = True
                break
        if not invalid:
            filtered_words.append(word)
    return filtered_words

possible_words = get_words_with_letters(words_with_nine_letters, letters_used)
print(possible_words)
print(len(possible_words))

def get_words_with_three_s(words):
    filtered_words  = []
    for word in words:
        letters = letter_count(word)
        if letters['s'] == 3:
            filtered_words.append(word)
    return filtered_words

triple_s_words = get_words_with_three_s(possible_words)
print(triple_s_words)
# This is a 5-gram or 25-gram (not likely)
# A 9-letter word with 5-grams have
# two letters that are repeated once
# two letters that are repeated twice
# two letters that are repeated three times
# two letters that are repeated four times
# 1 letter that is repeated five times
# There has to be three s'es


# aeteesasrsssstaesersrrsse
#
# 12345 23456 34567 45678 56789

a = 1 + 2, 3 == 1 + 2, 9 + 2, 1 + 8, 8 + 9, 3, 7
e = 1 + 5, 2 + 4, 3 + 3
r = 4, 2 + 2, 3 + 1
s = 5 + 3 + 2, 5 + 4 + 1
t = 1 + 1, 2
