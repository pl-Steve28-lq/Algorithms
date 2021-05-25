import heapq
Inf = 999999999

def heapSort(L):
  _ = []
  res = []
  for i in L: heapq.heappush(_, i)
  while _: res.append(heapq.heappop(_))
  return res

def Node(val):
  return [Inf, val, []]

# node = (cost: int, value: int, neighbors: tuple[n_cost: int, n_node: node])
def dijkstra(tnodes, nodes, prev={}):
  if not nodes: return tnodes, prev
  node = heapq.heappop(nodes)
  cost, value, neighbors = node

  neighbors = heapSort(neighbors)
  for n_cost, n_node in neighbors:
    val = n_node[1]

    new_cost = cost + n_cost
    if new_cost < tnodes[val][0]:
      tnodes[val][0] = new_cost
      prev[val] = value

  return dijkstra(tnodes, nodes, prev)

def main():
  Start = Node(0)
  Node1 = Node(1)
  Node2 = Node(2)
  Node3 = Node(3)
  Node4 = Node(4)
  End = Node(5)

  Start[0] = 0
  Start[2] = [(5, Node1), (8, Node2), (10, Node3)]
  Node1[2] = [(2, Node4), (1, Node2), (5, End)]
  Node2[2] = [(3, Node3), (6, End)]
  Node4[2] = [(2, End)]

  nodes = [Start, Node1, Node2, Node3, Node4, End]
  tnodes, prev = dijkstra(tuple(nodes), nodes)

  root = []
  i = 5
  while i != 0:
    root.append(i)
    i = prev[i]
  print(tnodes[5][0], root)

if __name__ == '__main__': main()
