#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[14]:


## Represents a single node in the Trie
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


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[ ]:





# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[15]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[16]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




