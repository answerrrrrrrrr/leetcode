class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # 60ms
        curSum = maxSum = 0
        for i in nums:
            curSum = max(0, curSum) + i
            maxSum = max(curSum, maxSum)
        return max(nums) if maxSum == 0 else maxSum

    # 80ms
        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum
    


    # DP
    # 60ms
        l = nums[:]
        for i in xrange(1, len(l)):
            l[i] = max(l[i], l[i]+l[i-1])
        return max(l)