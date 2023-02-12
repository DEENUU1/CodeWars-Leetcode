# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)

    return set(s.lower()) >= alphabet