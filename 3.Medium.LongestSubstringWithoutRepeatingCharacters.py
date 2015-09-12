class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    # 124ms
        sub, maxlen = '', 0
        for i in s:
            if i in sub:
                sub = sub[sub.index(i)+1:]
            sub += i
            if len(sub) > maxlen:
                maxlen = len(sub)
        return maxlen



# https://leetcode.com/discuss/51492/python-solution-with-comments
    # 108ms
        dic, head, maxlen = {}, 0, 0
        for i in range(len(s)):
            if s[i] in dic:
                maxlen = max(maxlen, i-head)
                head = max(head, dic[s[i]] + 1 )
            dic[s[i]] = i
        return max(maxlen, len(s)-head)

