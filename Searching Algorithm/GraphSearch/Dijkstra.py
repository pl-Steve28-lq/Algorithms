class Node:
  def __init__(self, value):
    self.value = value
    self.path = []

def _dijkstra(node, costs):
  neighbors = sorted(node.path, key=lambda x: x[1])
  
  for neighbor, cost in neighbors:
    val = neighbor.value
    costs[val] = min(costs[val], costs[node.value]+cost)

  for neighbor, _ in neighbors:
    costs = _dijkstra(neighbor, costs)

  return costs

def dijkstra(node, count):
  costs = { i : 314159265358979 for i in range(count) }
  costs[0] = 0

  return _dijkstra(node, costs)[count-1]

def main():
  Start = Node(0)
  One = Node(1)
  Two = Node(2)
  Three = Node(3)
  Four = Node(4)
  End = Node(5)

  Four.path = [(End, 2)]
  Two.path = [(Three, 3), (End, 6)]
  One.path = [(Two, 1), (Four, 2), (End, 5)]
  Start.path = [(One, 5), (Two, 8), (Three, 10)]

  print(dijkstra(Start, 6))

  if __name__ == '__main__': main()
