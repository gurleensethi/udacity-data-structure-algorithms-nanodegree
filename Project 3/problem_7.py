# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    def insert(self):
        pass

    def set_handler(self, handler):
      self.handler = handler

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):      
      current_node = self.root      

      splits = path.split("/")

      for split in splits:
        if split in current_node.children:
          current_node = current_node.children[split]
        else:
          new_node = RouteTrieNode()
          current_node.children[split] = new_node
          current_node = new_node
      
      current_node.set_handler(handler)

    def find(self, search):      
      splits = search.split("/")
      
      temp_node = self.root

      for split in splits:
        if split not in temp_node.children:
          return None
        temp_node = temp_node.children[split]
      
      return temp_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler = "not found handler"):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.trie.insert(path, handler)

    def lookup(self, path):
        handler = self.trie.find(path)

        if handler == None:
          return self.not_found_handler
        
        return handler


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test cases
router.add_handler("/home/about/me", "about me handler")
print(router.lookup("/home/about/me")) # should print 'about me handler'
router.add_handler("/home/about/me", "overriden about me handler")
print(router.lookup("/home/about/me")) # should print 'overriden about me handler'
router.add_handler("/home/", "home")
print(router.lookup("/home/")) # should print 'home'