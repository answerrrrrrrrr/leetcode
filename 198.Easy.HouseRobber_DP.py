class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
    # DP, O(n) space
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        res = [0] * n
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, n):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        return res[-1]



    # DP, O(1) space
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in xrange(2, n):
            a, b = b, max(a + nums[i], b)
        return b



    # DP, O(1) space
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now