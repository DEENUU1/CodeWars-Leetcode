# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

from collections import Counter


def duplicate_count(text):
    x = Counter(text.lower())
    count = 0
    for value in x.values():
        if value > 1:
            count += 1
    return count
