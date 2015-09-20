class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # WA
    # input           [2,1,1]
    # Your answer     [[1,1,2],[1,2,1],[1,2,1],[2,1,1]]
    # Expected answer [[1,1,2],[1,2,1],[2,1,1]]
        # if not nums:
        #     return [[]]
        # res = []
        # for p in self.permuteUnique(nums[1:]):
        #     for i in range(len(nums)+1):
        #         if nums[i] == nums[0]:
        #             continue
        #         res.append(p[:i] + nums[0] + p[i:])
        # return res

# https://leetcode.com/discuss/36740/120-ms-simple-python-solution-using-set-and-tuple
    # use set & tuple to avoid duplicates
    # 120ms
        if not nums:
            return [[]]
        return [list(i) for i in self.permuteInTuple(nums)]
    def permuteInTuple(self, nums):
        if not nums:
            return ((),)
        res = set()
        for p in self.permuteInTuple(nums[1:]):
            for i in range(len(p)+1):
                res.add(p[:i] + (nums[0],) + p[i:])
        return res



# https://leetcode.com/discuss/22575/iterative-python-solution-without-using-set-111ms
    # itr
    # 111ms
        res = [[]]
        for num in nums:
            newRes = []
            l = len(res[0])
            for p in res:
                for i in range(l, -1, -1):
                    if i < l and p[i] == num:
                        break
                    newRes.append(p[:i] + [num] + p[i:])
            res = newRes
        return res