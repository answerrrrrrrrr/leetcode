class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = s - target
                if diff == 0:
                    return target
                if diff > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                if diff < 0:
                    j += 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                if abs(ans-target) > abs(diff):
                    ans = s
        return ans
