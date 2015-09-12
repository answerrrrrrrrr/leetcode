class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        # while k > 0:
        #     nums.insert(0, nums.pop()) # too slow
        #     k -= 1
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]