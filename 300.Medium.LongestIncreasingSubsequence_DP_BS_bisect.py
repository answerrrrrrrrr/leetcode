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
    # O(n), zip
    # WA
        # dp = [1]
        # for i in xrange(1, len(nums)):
            # dp.append(max([y + 1 for x,y in zip(range(i),dp)
                                 # if nums[x] < nums[i]] or [1]))
        # return max(dp)



    # O(nlogn), BS
    # 48ms
        if not nums:
            return 0
        res = [nums[0]]
        for num in nums:
            if num > res[-1]:
                res.append(num)
            else:
                l, r = 0, len(res)-1
                while l < r:
                    m = (l+r)/2
                    if num > res[m]:
                        l = m+1
                    else:
                        r = m
                res[r] = num
        return len(res)



    # O(nlogn)
    # 48ms
        res = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l < r:
                m = (l+r)/2
                if res[m] < num:
                    l = m + 1
                else:
                    r = m
            res[r] = num
            size = max(size, r+1)
        return size



    # O(nlogn), bisect, inf
    # 48ms
        res = [float('inf')] * (len(nums)+1)
        for num in nums:
            res[bisect.bisect_left(res, num)] = num
        return res.index(float('inf'))
