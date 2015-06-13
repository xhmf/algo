
class TrieNode:

    def __init__(self, val = None):
        self.val = val
        self.children = {}

    def append(self, letter):
        if letter in self.children:
            return self.children[letter]
        child = TrieNode(letter)
        self.children[letter] = child
        return child

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = 0

    def add(self, word):
        current = self.root
        for letter in word:
            current = current.append(letter)
        if current.children == {}:
            self.words += 1

    def get_words(self):
        self.rec_words('', self.root)

    def rec_words(self, current, node):
        if node.children == {}:
            print current
        else:
            for key in node.children.keys():
                self.rec_words(current + key, node.children[key])

