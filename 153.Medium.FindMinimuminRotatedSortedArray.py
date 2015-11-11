class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # O(n)
        for i in xrange(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]



    # O(logn)
        i, j = 0, len(nums)-1
        while i < j:
            m = (i + j)/2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
        return nums[i]