class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        try:
            while 1:
                nums.remove(val)
        except:
            return len(nums)