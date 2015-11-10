class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    # traverse, O(n)
    # 68ms
        iZero = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[iZero] = nums[iZero], nums[i]
                iZero += 1



    # sort, key
    # 64ms
        nums.sort(key = lambda x: not x)
        # nums.sort(key = operator.not_)