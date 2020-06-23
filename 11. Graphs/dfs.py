class GraphNode:
  def __init__(self, val):
    self.value = val
    self.children = []

  def add_child(self, new_node):
    self.children.append(new_node)

  def remove_child(self, del_node):
    if del_node in self.children:
      self.children.remove(del_node)

class Graph:
  def __init__(self, node_list):
    self.nodes = node_list

  def add_edge(self, node1, node2):
    if (node1 in self.nodes and node2 in self.nodes):
      node1.add_child(node2)
      node2.add_child(node1)
    
  def remove_edge(self, node1, node2):
    if node1 in self.nodes and node2 in self.nodes:
      node1.remove_child(node2)
      node2.remove_child(node1)

def dfs_search(root_node, search_value):
  stack = [root_node]
  visited = set()

  while stack:
    current_node = stack.pop()
    visited.add(current_node)

    if current_node.value == search_value:
      return current_node

    for child in current_node.children:
      if child not in visited and child not in stack:
        stack.append(child)

  return False

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA])
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

dfs_search(nodeG, 'S')