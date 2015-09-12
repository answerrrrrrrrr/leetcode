class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    # leetcode.com/discuss/21550/my-3-lines-code-in-java-and-python
    # 60ms+
        # nums = [str(i) for i in nums]
        # nums.sort(lambda x,y: cmp(y+x, x+y))
        # return ''.join(nums).lstrip('0') or '0'
    # Simplified
        return ''.join(sorted(map(str, nums), lambda x,y: cmp(y+x, x+y))).lstrip('0') or '0'



    # Others
    # leetcode.com/discuss/53561/python-different-solutions-bubble-insertion-selection-sorts