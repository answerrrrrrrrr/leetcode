class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    # dict O(n)
    # Find an element in the dictionary only requires O(1) time.
    # 68ms
        d = {}
        for i, n in enumerate(nums, 1):
            # d[n] = i <--- CANNOT be here!!!
            if d.get(target-n, 0):
                return [d[target-n], i]
            d[n] = i # Avoid the case: n == target-n

    # 36ms
        d = {}
        for i in xrange(len(nums)):
            if target - nums[i] in d:
                return d[target - nums[i]]+1, i+1
            d[nums[i]] = i