class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
    # 2 dicts, dict.get
        s = str.split()
        if len(s) != len(pattern):
            return False
        d1, d2 = {}, {}
        for i in xrange(len(s)):
            d1[s[i]] = d1.get(s[i], len(d1))
            d2[pattern[i]] = d2.get(pattern[i], len(d2))
            if d1[s[i]] != d2[pattern[i]]:
                return False
        return True



    # lambda, map, dict.setdefault
        f = lambda s: map({}.setdefault, s, xrange(len(s)))
        return f(pattern) == f(str.split())



    # map, str.find, list.index
        p, s = pattern, str.split()
        return map(p.find, p) == map(s.index, s)



    # set, zip
        p, s = pattern, str.split()
        return len(p) == len(s) and len(set(zip(p, s))) == len(set(p)) == len(set(s))
            # zip([1,2], [1]) ---> [(1,1)]
            # so len(p) == len(s) is necessary