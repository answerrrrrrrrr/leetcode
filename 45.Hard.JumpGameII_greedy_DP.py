class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # greedy, DP
    # 60ms, 82.03%
        step, cur, fin = 0, 0, 0
        for i in xrange(len(nums)-1):
            cur = max(cur, i+nums[i])
            if fin == i and fin < cur:
                fin = cur
                step += 1
        return step
