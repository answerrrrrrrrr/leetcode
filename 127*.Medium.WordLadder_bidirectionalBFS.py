class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
# bidirectional BFS
    # 2 sets
    # https://leetcode.com/discuss/48083/share-python-solutions-concise-160ms-optimized-solution-100ms
        res, wordLen = 2, len(beginWord)
        src, dst = set([beginWord]), set([endWord])
        # wordList.discard(beginWord)
        while src:
            wordList -= src # avoid cycle
            src = wordList & (set(word[:i] + c + word[i+1:]
                                    for word in src
                                    for i in xrange(len(wordLen))
                                    # for c in 'qwertyuiopasdfghjklzxcvbnm'))
                                    for c in string.lowercase)) # import string
            if src & dst:
                return res
            res += 1
            if len(src) > len(dst):
                src, dst = dst, src
        return 0



    # deque
    # https://leetcode.com/discuss/63890/ac-python-two-solutions-based-on-two-end-bfs-144ms
