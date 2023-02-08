# https://www.codewars.com/kata/54da5a58ea159efa38000836

from collections import Counter


def find_it(seq):
    seq_counter = Counter(seq)
    odd = list(filter(lambda x: x % 2 != 0, seq_counter.values()))

    odd_to_int = int(odd[0])

    key_list = list(seq_counter.keys())
    values_list = list(seq_counter.values())

    position = values_list.index(odd_to_int)
    return key_list[position]