# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))