class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        read = '1'
        for _ in xrange(n-1):
            read = self.cas(read)
        return read
    
    def cas(self, read):
    # Wrong
        # ret = ''
        # count = digit = 0
        # for i in read:
        #     if i != digit:
        #         count, digit = 1, i
        #     else:
        #         count += 1
        #     ret += str(count) + str(digit)
        # return ret

    # Correct
        count, digit, ret = 0, '0', ''
        for i in read:
            if i != digit:
                if count:
                    ret += str(count) + digit
                count, digit = 1, i
            else:
                count += 1
        if count:
            ret += str(count) + digit
        return ret




# https://leetcode.com/discuss/48909/python-accepted-solution
    # def countAndSay(self, n):
    #     res = "1"
    #     for _ in xrange(n-1):
    #         res = self.helper(res)
    #     return res

    # def helper(self, n):
    #     count, i, res = 1, 0, ""
    #     while i < len(n) - 1:
    #         if n[i] == n[i+1]:
    #             count += 1
    #         else:
    #             res += str(count) + n[i]
    #             count = 1
    #         i += 1
    #     res += str(count) + n[i]
    #     return res