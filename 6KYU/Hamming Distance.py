# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69

def hamming(a,b):
    count = 0
    for i in range(len(a)):
        if b[i] != a[i]:
            count += 1
    return count