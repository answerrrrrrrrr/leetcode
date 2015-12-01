class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")



# defaultdict, itr
# 164ms
    def __init__(self):
        self.words = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.words[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        l = len(word)
        if '.' in word:
            for elword in self.words[l]:
                for i in xrange(l):
                    if elword[i] != word[i] and word[i] != '.':
                        break
                else:
                    return True
        return word in self.words[l]



# https://leetcode.com/discuss/36259/tree-solutions-18-20-lines
# trie, setdefault
# 500ms
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None


    # rcs
    def search(self, word):
        def find(word, node):
            if not word:
                return '$' in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid)
        return find(word, self.root)



    # itr
    def search(self, word):
        nodes = [self.root]
        for char in word + '$':
            nodes = [kid for node in nodes
                         for kid in
                            ([node[char]] if char in node
                                else filter(None, node.values())
                                if char == '.' else [])]
        return bool(nodes)

