class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Set (extra space)
    # 80ms+
        # nums[:] = sorted(list(set(nums)))
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)



    # Remove duplicated nums
    # 600ms+
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1



    # Override duplicated nums
    # 90ms+
        lastNum = None
        index = 0
        for i in nums:
            if i != lastNum:
                nums[index] = i
                index += 1
                lastNum = i
        return index

    # 80ms+
        if not nums:
            return 0
        lastIndex = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[lastIndex]:
                nums[lastIndex+1] = nums[i]
                lastIndex += 1
        return lastIndex + 1




















