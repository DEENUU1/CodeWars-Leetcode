# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

from collections import Counter

def duplicate_encode(word):
    counter = Counter(word.lower())
    new_word = []
    for character in word.lower():
        if counter[character] == 1:
            new_word.append('(')
        else:
            new_word.append(')')
    return "".join(new_word)
