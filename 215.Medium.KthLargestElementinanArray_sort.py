class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    # sorted_reverse
        return sorted(nums, reverse=True)[k-1]



# https://leetcode.com/discuss/53530/python-different-solutions-comments-bubble-selection-quick