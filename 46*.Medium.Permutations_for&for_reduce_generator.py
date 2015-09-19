class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # rcs
    # 80ms
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            tails = self.permute(nums[:i] + nums[i+1:])
            for tail in tails:
                res += [nums[i]] + tail,
        return res

    # rcs gen
    # 80ms
        def gen(nums):
            if not nums:
                yield []
            for i in range(len(nums)):
                for j in gen(nums[:i] + nums[i+1:]):
                    yield [nums[i]] + j
        return list(gen(nums))

# https://leetcode.com/discuss/42550/one-liners-in-python
# one-liners

    # Solution 1: Recursive, take any number as first
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]



    # Solution 2: Recursive, insert first number anywhere
    # the most fast one
    # 136ms for [1,2,3,4,5,6,7] while approachs above using 160ms+
        return nums and [p[:i] + [nums[0]] + p[i+1:] 
                        for p in self.permute(nums[1:]) 
                        for i in range(len(nums))] or [[]]



    # Solution 3: Reduce, insert next number anywhere
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                        for p in P
                                        for i in range(len(p)+1)],
                        nums, [[]])



    # Solution 4: Using the library
        return list(itertools.permutations(nums))
        # return map(list, itertools.permutations(nums))