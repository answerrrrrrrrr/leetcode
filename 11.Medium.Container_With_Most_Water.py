class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p, q = 0, len(height)-1
        ret = 0
        while p < q:
            ret = max(ret, (q-p) * min(height[p], height[q]))
            if height[p] < height[q]:
            # https://leetcode.com/discuss/31210/a-question-for-this-problem?show=34767#a34767
            # Why not use height[p+1] > height[q-1]
                p += 1
            else:
                q -= 1
        return ret
