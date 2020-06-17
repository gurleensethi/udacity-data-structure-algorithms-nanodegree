# Problem 5

To solve this problem I have first created the trie.
Each character of a word is represented as a node in the tree.

All the possible suffixes are calculated using DFS.
Once you have the required node with the given prefix, run DFS on that
node and find all the suffixes below the given node.

The time complexity is O(N \* L) where N is the total number of nodes inside the
tree, and L is the length of word being search (strings need to matched for comparison).

The space complexity is O(W \* L) where W is the total number of words that
can be formed from the trie, and L is the length of a longest word.
