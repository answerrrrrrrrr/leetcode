class Solution(object):
# https://leetcode.com/discuss/52722/short-and-o-n-python-and-c
    
    # 60ms+
    # uglyNums = sorted(2**a * 3**b * 5**c 
    #     for a in xrange(32) for b in xrange(20) for c in xrange(14))
    # def nthUglyNumber(self, n):
    #     return self.uglyNums[n-1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
    # 230ms+
        uglyNums = [1]
        i2 = i3 = i5 = 0
        while len(uglyNums) < n:
            uglyNums.append(min(uglyNums[i2]*2, uglyNums[i3]*3, uglyNums[i5]*5))
            if uglyNums[-1] == uglyNums[i2]*2:
                i2 += 1
            if uglyNums[-1] == uglyNums[i3]*3:
                i3 += 1
            if uglyNums[-1] == uglyNums[i5]*5:
                i5 += 1
        return uglyNums[-1]



# https://leetcode.com/discuss/52711/python-solution-using-dp
# Dynamic Programming
    # 180ms+
        uglyNums = [1] * n 
        i2 = i3 = i5 = 0
        next2, next3, next5 = uglyNums[i2]*2, uglyNums[i3]*3, uglyNums[i5]*5
        for i in xrange(1, n):
            cur = uglyNums[i] = min(next2, next3, next5)
            if cur == next2:
                i2 += 1
                next2 = uglyNums[i2] * 2
            if cur == next3:
                i3 += 1
                next3 = uglyNums[i3] * 3
            if cur == next5:
                i5 += 1
                next5 = uglyNums[i5] * 5
        return uglyNums[-1]







        