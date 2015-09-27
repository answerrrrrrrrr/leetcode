class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
# https://leetcode.com/discuss/49407/python-easy-to-understand-solution-with-dictionary
    # dic
    # 248ms
        dic = {}
        for s in strs:
            i = tuple(sorted(s))
            dic[i] = dic.get(i, []) + [s]
        return [sorted(i) for i in dic.values()]



# https://leetcode.com/discuss/51190/1-line-ruby-python-for-updated-problem
    # collections.defaultdict
    # 268ms
        dd = collections.defaultdict(list)
        for s in strs:
            dd[tuple(sorted(s))].append(s)
        return [sorted(i) for i in dd.values()]
        # return map(sorted, dd.values()) ---> a bit slower



    # itertools.groupby
    # 288ms
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        # >>> strs
        # ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

        # >>> sorted(strs)
        # ['ate', 'bat', 'eat', 'nat', 'tan', 'tea']

        # >>> sorted(strs, key=sorted)
        # ['bat', 'eat', 'tea', 'ate', 'tan', 'nat']

        # >>> groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        # >>> groups
        # <itertools.groupby object at 0x102817fc8>

        # >>> for i in groups:
        # ...     print i
        # ...
        # (['a', 'b', 't'], <itertools._grouper object at 0x10282a790>)
        # (['a', 'e', 't'], <itertools._grouper object at 0x10282a850>)
        # (['a', 'n', 't'], <itertools._grouper object at 0x10282a790>)
        return [sorted(group) for _, group in groups]