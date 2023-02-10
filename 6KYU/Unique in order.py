# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    lst = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            lst.append(sequence[i])
    return lst