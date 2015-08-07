class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or '' in strs:
            return ''
        lcp = ''
        for l in zip(*strs):
            if len(set(l)) == 1:
                lcp += l[0]
            else:
                break
        return lcp