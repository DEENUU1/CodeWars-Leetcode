# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    lst = sentence.split(" ")
    result = [x[::-1] if len(x) >= 5 else x for x in lst ]
    return " ".join(result)