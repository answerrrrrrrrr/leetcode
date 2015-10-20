class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
# https://leetcode.com/discuss/223/when-there-are-duplicates-the-worst-case-is-could-we-do-better
# https://leetcode.com/discuss/50068/python-easy-to-understand-solution-with-comments
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)/2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False