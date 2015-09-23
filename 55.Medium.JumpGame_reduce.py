class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
# https://leetcode.com/discuss/41420/1-6-lines-o-n-time-o-1-space
    # going forwards
    # 52ms
        m = 0
        for i, e in nums:
            if i > m:
                return False
            m = max(m, i+e)
        return True



    # reduce
    # 68ms
        return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0



    # going backwards
    # 52ms
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal