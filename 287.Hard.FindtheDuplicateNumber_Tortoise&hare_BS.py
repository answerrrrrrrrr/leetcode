class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# ~ 142.Linked List Cycle II
# Tortoise and hare
# https://leetcode.com/discuss/61033/concise-python-solution-tortoise-and-hare-o-n
        slow, fast, ret = nums[0], nums[nums[0]], 0
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        while slow != ret:
            slow, ret = nums[slow], nums[ret]
        return ret



# binary search
# https://leetcode.com/discuss/61964/simple-5-line-python-solution-using-binary-search
        l, r = 1, len(nums)-1
        while l < r:
            m = (l+r)/2
            l, r = [l, m] if sum(num <= m for num in nums) > m else [m+1, r]
        return r
