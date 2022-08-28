from heapq import*
inf = float('inf')

N = 5
graph = {1: [(6, 3), (3, 4)], 2: [(3, 1)], 3: [(2, 4)], 4: [(1, 2), (1, 3)], 5: [(4, 2), (2, 4)]}

def dijkstra(start, end):
  dist = [inf]*(N+1)
  heap = [(0, start)]
  while heap:
    cur_cost, node = heappop(heap)
    for cost, i in graph[node]:
      c = cur_cost + cost
      if c < dist[i]:
        dist[i] = c
        heappush(heap, (c, i))
  return dist[end]

print(dijkstra(1, 2))
