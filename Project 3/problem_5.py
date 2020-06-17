# To solve this problem I have first created the trie.
# Each character of a word is represented as a node in the tree.
# 
# All the possible suffixes are calculated using DFS. 
# Once you have the required node with the given prefix, run DFS on that
# node and find all the suffixes below the given node.
#
# The time complexity is O(N) where N is the total number of nodes inside the
# tree. The space complexity is O(W * L) where W is the total number of words that
# can be formed from the trie, and L is the length of a longest word.

class TrieNode:
  def __init__(self, is_word = False):
    self.is_word = is_word
    self.children = dict()

  def insert(self, char):
    pass

  def set_word(self, is_word):
    self.is_word = is_word

  def suffixes(self, suffix = ''):
    suffixes = []

    if self.is_word and suffix != '':
      suffixes.append(suffix)

    for c in self.children:
      suffixes.extend(self.children[c].suffixes(suffix + c))

    return suffixes

class Trie:
  def __init__(self):
    self.root = TrieNode()    

  def insert(self, word):
    current_node = self.root

    for c in word:
      if c in current_node.children:
        current_node = current_node.children[c]
      else:
        new_node = TrieNode()
        current_node.children[c] = new_node
        current_node = new_node
    
    current_node.set_word(True)

  def find(self, prefix):
    current_node = self.root

    for c in prefix:
      if c in current_node.children:
        current_node = current_node.children[c]
      else:
        return None

    return current_node
