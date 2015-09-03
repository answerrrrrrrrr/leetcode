class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        p, q = 0, len(s)-1
        res = []
        temp = None
        while p < q-1:
            l, s[p] = s[p], None
            r, s[q] = s[q], None
            c = -(l + r)
            print (l,c,r)
            if c in s and [l, c, r] not in res :
                res.append([l, c, r])
            if c < 0:
                s[p] = l
                q -= 1
            else:
                s[q] = r
                p += 1
                if c == 0:
                    temp = l
            if temp and -temp not in s:
                p -= 1
                s[p] = temp
                temp = None
        return res