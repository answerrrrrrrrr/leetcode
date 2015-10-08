class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    # head & tail
    # 40ms
        l, c, r = 0, 0, len(nums)-1
        while c <= r:
            if nums[c] == 0:
                nums[c], nums[l] = nums[l], nums[c]
                c+=1; l+=1
            # if nums[c] == 2: --> WA:list index out of range
            elif nums[c] == 2: 
                nums[c], nums[r] = nums[r], nums[c]
                r-=1
            else:
                c+=1



# https://leetcode.com/discuss/62048/python-in-place-one-pass-solution-time-space-no-swap-no-count
    # Lomuto Partition
    # 40ms
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1