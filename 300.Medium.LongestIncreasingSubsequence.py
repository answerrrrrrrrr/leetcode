
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # dict, max
    # 464ms
        d = {}
        for num in nums:
            maxVal = max([0] + [d[k] for k in d if k < num])
            d[num] = maxVal+1
        return max([0] + d.values())



    # DP
        dp = [1]
        for i in xrange(1, len(nums)):
            dp.append(max([y + 1 for x,y in zip(range(i),dp) 
                                 if nums[x] < nums[i]] or [1]))
        return max(dp)
