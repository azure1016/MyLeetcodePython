from collections import defaultdict
import collections


class TrieNode:
    def __init__(self):
        self.ch = defaultdict(TrieNode)
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.ch[c]
        node.isEnd = True

    def _startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.ch: return False, node.ch[c]
        return True, node

    def startsWith(self, prefix):
        isPrefix, node = self._startsWith(prefix)
        return isPrefix

    def search(self, word):
        isPrefix, node = self._startsWith(word)
        return isPrefix and node.isEnd

obj = Trie()
obj.insert("app")
obj.insert("apple")
param_2 = obj.search("app")
param_4 = obj.search('apple')
param_3 = obj.startsWith("app")