# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    odds = sorted([x for x in source_array if x%2 != 0])
    return [x if x %2 == 0 else odds.pop(0) for x in source_array] 