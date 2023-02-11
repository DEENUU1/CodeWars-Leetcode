# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        x = ''.join(i for i in s if i.isalnum())
        if x.lower() == x[::-1].lower():
            return True
        return False
