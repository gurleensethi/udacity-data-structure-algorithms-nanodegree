class Node:
  def __init__(self, value, parent, color):
    self.value = value
    self.parent = parent
    self.color = color
    self.left = None
    self.right = None

class RedBlackTree:
  def __init__(self, value):
    self.root = Node(value, None, 'red')

  def insert(self, value):
    new_node = self.insert_helper(self.root, value)
    print(new_node.value)

  def insert_helper(self, current, new_val):
    if new_val < current.value:
      if current.left:
        return self.insert_helper(current.left, new_val)
      else:
        current.left = Node(new_val, current, 'red')
        return current.left
    else:
      if current.right:
        return self.insert_helper(current.right, new_val)
      else:
        current.right = Node(new_val, current, 'red')
        return current.right

    def rebalance(self, node):
      if node.parent == None:
        return
      
      if node.parent.color == "black":
        return

      if pibling(node).color == "red":
        pibling(node).color = "black"
        node.parent.color = "black"
        grandparent(node).color = "red"
        self.rebalance(grandparent(node))

  def search(self, value):
    return False

red_black_tree = RedBlackTree(10)
red_black_tree.insert(1)
red_black_tree.insert(1123)
red_black_tree.insert(2)
red_black_tree.insert(45)
red_black_tree.insert(6)