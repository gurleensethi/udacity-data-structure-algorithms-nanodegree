class TrieNode:
  def __init__(self):
    self.is_word = False
    self.children = {}  

  def __str__(self):
    return f"{self.children} / {self.is_word}"

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def add(self, word):
    current_node = self.root

    for index, char in enumerate(word):      
      if char in current_node.children:
        current_node = current_node.children[char]
      else:
        new_node = TrieNode()        
        current_node.children[char] = new_node
        current_node = new_node
    
    current_node.is_word = True

  def exists(self, word):
    temp = self.root

    for char in word:
      if char in temp.children:
        temp = temp.children[char]
      else:
        break

    return temp.is_word

trie = Trie()
trie.add('Testing')
trie.add('Test')
trie.add('Another')
print(trie.exists('Testing'))
print(trie.exists('Test'))
print(trie.exists('Another'))