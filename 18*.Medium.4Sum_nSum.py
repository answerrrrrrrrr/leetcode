class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
# https://leetcode.com/discuss/54724/python-140ms-beats-100%25-and-works-for-n-sum-n-2
# nSum
    # 130ms
        nums.sort()
        res = []
        self.nSum(nums, target, 4, [], res)
        return res
    def nSum(self, nums, target, N, leftItems, res):
        numsLen = len(nums)
        if numsLen < N or N < 2:
            return
        if N == 2:
            l, r = 0, numsLen-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(leftItems + [nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(numsLen - N + 1):

                # The most AWESOME part of this solution
                # take adventage of sorted list
                # runtime: 1000ms+ ---> 100ms+
                if target < nums[i] * N or target > nums[-1] * N:
                    break

                if i == 0 or nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target-nums[i], N-1, leftItems + [nums[i]], res)
        # return