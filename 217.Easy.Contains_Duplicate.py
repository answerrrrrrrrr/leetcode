class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
    	# # Time Limit Exceeded
    	# for i, n in enumerate(nums):
     #        if i != nums.index(n):
     #            return True
     #    return False
        return len(set(nums)) < len(nums)