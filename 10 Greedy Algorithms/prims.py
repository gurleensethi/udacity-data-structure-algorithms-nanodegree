import heapq

class Graph:
  def __init__(self):
    self.nodes = set()
    self.graph = {}

  def add_node(self, node):
    self.nodes.add(node)
    
    if node not in self.graph:
      self.graph[node] = []
  
  def add_edge(self, nodeA, nodeB, cost):
    self.add_node(nodeA)
    self.add_node(nodeB)

    self.graph[nodeA].append((nodeB, cost))
    self.graph[nodeB].append((nodeA, cost))

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = Graph()

    for nodeA, nodeB, cost in bridge_config:
      graph.add_edge(nodeA, nodeB, cost)

    visited = set()
    min_heap = []
    total_cost = 0

    heapq.heappush(min_heap, (0, bridge_config[0][0]))

    while min_heap:
      cost, vertex = heapq.heappop(min_heap)

      if vertex not in visited:        
        total_cost += cost

        for node, cost in graph.graph[vertex]:
          if node not in visited:
            heapq.heappush(min_heap, (cost, node))

        visited.add(vertex)

    return total_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)