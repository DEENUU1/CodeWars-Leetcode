# https://www.codewars.com/kata/5208f99aee097e6552000148

import re

def solution(s):
    new_s = re.sub(r"([A-Z])", r" \1", s).strip()
    return new_s