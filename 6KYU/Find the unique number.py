# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

from collections import Counter


def find_uniq(arr):
    arr_counter = Counter(arr)

    keys = [k for k, v in arr_counter.items() if v == 1]
    new_lst = []
    for key in keys:
        new_lst.append(str(key))
    lst_to_str = ''.join(new_lst)
    return float(lst_to_str)