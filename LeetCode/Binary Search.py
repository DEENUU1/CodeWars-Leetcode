# https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        return nums.index(target)