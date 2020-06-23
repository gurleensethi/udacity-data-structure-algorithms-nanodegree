# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance

# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

import math
import sys

def dijkstra(graph, start_node, end_node):
    visited = set()
    remaining = set(graph.nodes)
    path = {}
    distances = {}

    for node in graph.nodes:
      distances[node.value] = sys.maxsize

    distances[start_node.value] = 0

    while remaining:
      current_node = None

      for node in remaining:
        if current_node == None:
          current_node = node
        elif distances[current_node.value] > distances[node.value]:
          current_node = node
      
      if node is None:
        break

      for edge in current_node.edges:
        if edge.node in remaining:          
          if edge.node not in distances or distances[current_node.value] + edge.distance < distances[edge.node.value]:
            distances[edge.node.value] = distances[current_node.value] + edge.distance
      
      remaining.remove(current_node)
    
    return distances[end_node.value]
      