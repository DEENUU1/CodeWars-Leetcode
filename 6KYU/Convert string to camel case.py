# https://www.codewars.com/kata/517abf86da9663f1d2000003

import re

def to_camel_case(text):
    if not text:
        return text

    words = re.findall(r'[A-Za-z][a-z]*', text)
    return words[0] + ''.join(word.title() for word in words[1:])