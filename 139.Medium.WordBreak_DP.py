class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
    # DP
        match = [0] 
        for i in xrange(1, len(s)+1):
            for j in reversed(match):
                if s[j:i] in wordDict:
                    match.append(i)
                    break
        return match[-1] == len(s)