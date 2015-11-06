class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # DP, O(n) space
        if len(nums) == 1:
            return nums[0]
        h = self.helper
        return max(h(nums[:-1]), h(nums[1:]))
    def helper(self, nums):
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
        if len(nums) == 1:
            return nums[0]
        h = self.helper
        return max(h(nums[:-1]), h(nums[1:]))
    def helper(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in xrange(2, n):
            a, b = b, max(b, a + nums[i])
        return b



    # DP, code optimized, O(1) space
        def h(nums):
            a, b = 0, 0
            for n in nums:
                a, b = b, max(b, a + n)
            return b
        return max(h(nums[:-1]), h(nums[len(nums) != 1 :]))