class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # itertools
        res = []
        for k in range(len(nums)+1):
            res += list(itertools.combinations(sorted(nums), k))
        return res
    # one-liner
        return reduce(lambda x,y: x+y, [list(itertools.combinations(sorted(nums), k)) for k in range(len(nums)+1)])



    # rcs
    if not nums:
            return [[]]
        nums.sort()
        tail = nums.pop()
        pre = self.subsets(nums)
        return [item + [tail] for item in pre] + pre



# https://leetcode.com/discuss/47717/understand-solutions-recursively-manipulation-iteratively
    # itr
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res 

    # rcs

    # bit manipulation