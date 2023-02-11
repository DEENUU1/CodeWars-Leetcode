# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = []
        count = 0
        for i in nums:
            count += i
            total.append(count)
        return total