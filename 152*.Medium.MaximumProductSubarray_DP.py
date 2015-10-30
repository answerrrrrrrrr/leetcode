class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 # https://leetcode.com/discuss/64079/my-concise-dp-o-n-java-solution-with-o-1-extra-space



    # DP
        res = maxP = minP = nums[0]
        for i in xrange(1, len(nums)):
            tempTuple = nums[i], maxP * nums[i], minP * nums[i]
            maxP, minP = max(tempTuple), min(tempTuple)
            res = max(maxP, res)
        return res



    # 1-liner DP
        return max(reduce(lambda A, n: [max(A), min(n, A[1]*n, A[2]*n), max(n, A[1]*n, A[2]*n)], nums[1:], [nums[0]]*3))