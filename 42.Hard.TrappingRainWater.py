class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
# https://leetcode.com/discuss/78651/my-easy-understood-one-pass-13-lines-python-solution
# 52ms, 80.67%
        if not height:
            return 0
        iMaxHeight = height.index(max(height))
        count = 0
        for i in xrange(iMaxHeight):
            if height[i] > height[i+1]:
                count += height[i] - height[i+1]
                height[i+1] = height[i]
        for i in xrange(len(height)-1, iMaxHeight, -1):
            if height[i] > height[i-1]:
                count += height[i] - height[i-1]
                height[i-1] = height[i]
        return count



# https://leetcode.com/discuss/26375/python-solutions-o-n-space-and-o-1-space
# 48ms, 94,80%
        l, r = 0, len(height)-1
        left = right = count = 0
        while l <= r:
            left, right = max(height[l], left), max(height[r], right)
            while l <= r and height[l] <= left <= right:
                count += left - height[l]
                l += 1
            while l <= r and height[r] <= right <= left:
                count += right - height[r]
                r -= 1
        return count



# https://leetcode.com/discuss/45812/7-lines-c-c
# 56ms, 61.34%
        l, r = 0, len(height)-1
        level = count = 0
        while l <= r:
            if height[l] < height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1
            level = max(lower, level)
            count += level - lower
        return count
