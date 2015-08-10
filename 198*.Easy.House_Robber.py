class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now