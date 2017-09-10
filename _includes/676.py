class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = None

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.s = {}
        for word in dict:
            for i in range(len(word)):
                self.s.setdefault(word[:i] + '_' + word[i+1:], set()).add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            n = word[:i] + '_' + word[i+1:]
            if n in self.s:
                if len(self.s[n]) > 1 or word not in self.s[n]:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
