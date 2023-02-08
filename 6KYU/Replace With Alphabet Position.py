# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    alb = 'abcdefghijklmnopqrstuvwxyz'
    if type(text) == str:
        result = ""
        text = text.lower()
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alb.index(letter) + 1)
        return result.lstrip(' ')
