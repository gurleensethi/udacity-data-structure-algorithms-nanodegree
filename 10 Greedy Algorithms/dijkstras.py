from collections import defaultdict
import sys

class Graph:
  def __init__(self):
    self.nodes = set()
    self.neighbours = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.neighbours[from_node].append(to_node)
    self.neighbours[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

  def print_graph(self):
    print("set of nodes", self.nodes)
    print("neighbours are", self.neighbours)
    print("distance are", self.distances)

def dijkstra(graph, source):
  unvisited = set(graph.nodes)
  result = {}
  path = {}

  for node in unvisited:
    result[node] = sys.maxsize
  
  result[source] = 0

  while unvisited:
    min_node = None

    for node in unvisited:
      if min_node == None:
        min_node = node
      elif result[node] < result[min_node]:
        min_node = node
    
    for neighbour in graph.neighbours[min_node]:
      if neighbour in unvisited:
        distance = result[min_node] + graph.distances[(min_node, neighbour)]

        if neighbour not in result or distance < result[neighbour]:
          print(min_node, "setting distance for", neighbour, "which is", distance)
          result[neighbour] = distance
          path[neighbour] = min_node
    
    unvisited.remove(min_node)

    if min_node == None:
      break
  
  return result

testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

print(dijkstra(testGraph, 'A'))