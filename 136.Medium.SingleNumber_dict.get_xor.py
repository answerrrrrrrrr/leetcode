class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # dict.get
    # O(n) space
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key



    # set & sum
    # O(1) space
        return 2*sum(set(nums))-sum(nums)



    # xor lambda
    # in place
        return reduce(lambda x, y: x ^ y, nums)

    # xor operator
    # in place
        return reduce(operator.xor, nums)