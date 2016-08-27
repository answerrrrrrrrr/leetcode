class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        # try:
        #     while 1:
        #         nums.remove(val)
        # except:
        #     return len(nums)

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i
