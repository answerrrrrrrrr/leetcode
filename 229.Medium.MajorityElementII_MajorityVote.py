class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    # MajorityVote
    # O(n) time, O(1) space
        if not nums:
            return []
        vote1, vote2, candi1, candi2 = 0, 0, 0, 1 # avoid duplicates
        for n in nums:
            if n == candi1:
                vote1 += 1
            elif n == candi2:
                vote2 += 1
            elif vote1 == 0:
                vote1, candi1 = 1, n
            elif vote2 == 0:
                vote2, candi2 = 1, n
            else:
                vote1 -= 1
                vote2 -= 1
        return [n for n in (candi1, candi2) if nums.count(n) > len(nums)/3]

# https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration?show=48973#a48973
