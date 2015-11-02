class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
# bucket/bin sort
# numbers in range [x-t, x+t] are mapped to range [x//t-1, x//t+1]

    # OrderedDict
    # 132ms
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            # save the code but waste time
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False) 
                # OrderedDict.popitem(last=True)
                # pop the last item with no argu or True
                # pop the first item with False
            dic[key] = n
        return False



    # Dict
    # 52ms
        if t < 0:
            return False
        n = len(nums)
        d = {}
        t += 1
        for i in xrange(n):
            if i > k:
                del d[nums[i - k - 1] / t]
            m = nums[i] / t
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < t:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < t:
                return True
            d[m] = nums[i]
        return False



# https://leetcode.com/discuss/42707/python-without-dictionary
    # sorted, key
    # 64ms
        n = len(nums)
        ind = sorted(range(n), key = lambda x: nums[x])
        for i in range(n-1):
            j = i+1 
            while j < n and nums[ind[j]] - nums[ind[i]] <= t:
                if abs(ind[i]-ind[j]) <= k:
                    return True
        return False