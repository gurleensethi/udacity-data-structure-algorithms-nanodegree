# Problem 7

The parts of urls are stored as nodes in a trie.
When a lookup is done, the path is split using "/" as separator.
For each part we traverse down the trie until we find the handler or
we have no further nodes to go to.

The time complexity of search is O(N) where N is the number of parts in
the url. If the url has 3 parts (for example, /a/b/c) it will only take
3 hops to reach the desired handler.
