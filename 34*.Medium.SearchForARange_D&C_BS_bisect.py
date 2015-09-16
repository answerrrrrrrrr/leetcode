class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# O(logn)
# https://leetcode.com/discuss/40921/9-11-lines-o-log-n
    # bisect
        import bisect
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_right(nums, target) - 1
        return [lo, hi] if target in nums[lo:lo+1] else [-1, -1]

    # BS
        n = len(nums)
        def binsearch(target):
            l, r = 0, n # NOT n-1 !!!
            while l < r:
                m = (l+r)/2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l 
        lo = binsearch(target)
        hi = binsearch(target+1)-1
        return [lo, hi] if target in nums[lo:lo+1] else [-1, -1]

    # D&C
        def binsearch(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                m = (lo + hi)/2
                l, r = binsearch(lo, m), binsearch(m+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return binsearch(0, len(nums)-1)