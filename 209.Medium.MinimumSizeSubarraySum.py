class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
    # O(n), 2 points
        l = r = 0
        ans = len(nums)
        cursum = 0
        while r < len(nums):
            cursum += nums[r]
            r += 1
            if cursum >= s:
                while cursum - nums[l] >= s:
                    cursum -= nums[l]
                    l += 1
                ans = min(ans, r-l)
        # return ans if sum(nums) >= s else 0
        return ans if cursum >= s else 0



    # O(n), 1 point
        minLen, cursum, l = len(nums)+1, 0, 0
        for i in xrange(len(nums)):
            cursum += nums[i]
            while cursum >= s:
                minLen, cursum, l = min(minLen, i+1-l), cursum - nums[l], l+1
        return 0 if minLen > len(nums) else minLen



    # O(nlogn)
    # O(n) space
        def findnewl(l, r, nums, v, s):
            while l < r:
                m = (l+r)/2
                if v - nums[m] >= s:
                    l = m + 1
                else:
                    r = m
            return l
        ans = len(nums)+1
        for i, v in enumerate(nums[1:], 1):
            nums[i] += nums[i-1]
        l = 0
        for r, v in enumerate(nums):
            if v >= s:
                l = findnewl(l, r, nums, v, s)
                ans = min(ans, r+1-l)
        return 0 if ans > len(nums) else ans
