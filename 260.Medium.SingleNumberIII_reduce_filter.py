class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
# 两个相等的数异或结果为0，因此，异或结果只与Single Number A,B有关
# 首次扫描数组，得到的结果即A、B异或的结果xor
# 因为A和B不相等，因此xor一定不为0，且二进制位为1的位A和B一定不同
# 任取xor中的一个二进制位(比如最右的1)，可以将原数组元素分成两组异或即得结果
        xor = reduce(operator.xor, nums)
        # Find the rightmost '1'
        # rightmost = 1
        # while xor & rightmost == 0:
        #     rightmost <<= 1
        rightmost = xor & -xor # -xor为补码，&后恰好可得rightmost
        a = b = 0
        for num in nums:
            if rightmost & num:
                a ^= num 
            else:
                b ^= num 
        return [a, b]



# https://leetcode.com/discuss/52387/3-line-python-code
        # Code Simplified
        xor = reduce(operator.xor, nums)
        a = reduce(operator.xor, filter(lambda x: x & xor & -xor, nums))
        return [a, a ^ xor]



        # Generator instead of Filter(too slow)
        xor = reduce(operator.xor, nums)
        a = reduce(operator.xor, [x for x in nums if x & xor & -xor])
        return [a, a ^ xor]