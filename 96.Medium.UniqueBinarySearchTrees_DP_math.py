class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
# https://leetcode.com/discuss/47960/python-solutions-dp-catalan-number
    # https://leetcode.com/discuss/24282/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i
    # DP
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1): # i numbers
            for j in xrange(i):  # j as root
                res[i] += res[j] * res[i-1-j]
        return res[n]



    # Catalan Number  (2n)!/((n+1)!*n!)  
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))