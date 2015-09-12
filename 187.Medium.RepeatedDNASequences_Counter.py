class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
# https://leetcode.com/discuss/35865/possible-the-shortest-python-code
    # 2 sets
    # 110ms
        once, twice = set(), set()
        for i in xrange(len(s)-9):
            subs = s[i:i+10]
            # if subs in once:
            #     twice.add(subs)
            # else:
            #     once.add(subs)
            (once, twice)[subs in once].add(subs)
        return list(twice)

    # 2 dicts
    # 110ms
        # d = {},{}
        # for i in xrange(len(s)-9):
        #     subs = s[i:i+10]
        #     d[subs in d[0]][subs] = None
        # return list(d[1])

    # 1 dict
    # 160ms
        # d = {}
        # for i in s[x:x+10] for x in range(len(s)-9):
        #     d[i] = d.get(i, 0) + 1
        # return [k for k,v in d.iteritems() if v > 1]

    # counter
    # 172ms
        c = collections.Counter(s[i:i+10] for i in xrange(len(s)-9))
        return [k for k in c if c[k] > 1]
