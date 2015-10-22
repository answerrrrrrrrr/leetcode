class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # itr
    # 76ms
        res = [[]]
        nums.sort()
        for num in nums: 
            res += [i+[num] for i in res if i+[num] not in res]
        return res

    # 56ms
        res = [[]]
        nums.sort()
        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in xrange(len(res)-l, len(res)):
                res.append(res[j] + [nums[i]])
        return res



    # rcs
    # 64ms
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)

    # rcs
    # 64ms
        def dfs(nums, path, res):
            res.append(path)
            for i in xrange(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path+[nums[i]], res)
        res = []
        nums.sort()
        dfs(nums, [], res)
        return res


