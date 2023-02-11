# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        size = len(x_string)
        y = x_string[size::-1]
        if str(y) == str(x):
            return True
        else:
            return False