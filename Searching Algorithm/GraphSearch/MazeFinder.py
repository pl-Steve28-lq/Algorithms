Inf = 99999999

class Node:
  def __init__(self, value):
    self.value = value
    self.path = []

def dijkstra(nodes, start, costs, visited, prev={}):
  node = nodes[start]
  visited[node.value] = True
  
  neighbors = sorted(node.path, key=lambda x: x[1])
  
  for neighbor, cost in neighbors:
    val = neighbor.value
    
    new_cost = costs[node.value]+cost
    
    if new_cost < costs[val]:
      costs[val] = new_cost
      prev[val] = node.value

  if sum(visited) == len(nodes): return costs, prev
  
  L = list(map(lambda x: costs[x]+Inf*visited[x], costs.keys()))
  return dijkstra(nodes, L.index(min(L)), costs, visited, prev)

def findPath(nodes, count, info):
  start, end = info
  
  costs = { i : Inf for i in range(count) }
  costs[start] = 0
  
  path_set = dijkstra(nodes, start, costs, [False]*count)[1]
  path = []
  
  i = end
  while i != start:
    path.append(i)
    i = path_set[i]
  path.append(start)
  return list(reversed(path))


class Maze:
  Path = '~'
  Wall = '0'
  Start = '+'
  End = '='

class SafeList(list):
  def get(self, *idx):
    length = len(self)
    try:
      if len(idx) == 1:
        if idx[0] >= 0: return self[idx[0]]
        raise Exception
      first, *other = idx
      return self[first].get(*other)
    except: return None

def findMaze(m):
  m = SafeList(map(SafeList, m.strip().split('\n')))
  X, Y = len(m[0]), len(m)
  idx = [[-1]*X for i in range(Y)]
  cur = 0
  info = [(-1, -1), (-1, -1)]
  direction = ((0, -1), (1, 0), (0, 1), (-1, 0))
  node = []
  
  for x in range(X):
    for y in range(Y):
      z = m[x][y]
      
      if z == Maze.Path:
        check = [0, 0]
        k = 0
        for i, j in direction:
          if m.get(x+i, y+j) not in [Maze.Wall, None]:
            check[k%2] += 1
          k += 1
          
        if tuple(check) in [(0, 2), (2, 0)]: continue
        idx[x][y] = cur
        cur += 1
        node.append((x, y))
        
      if z in Maze.Start + Maze.End:
        idx[x][y] = cur
        info[z == Maze.End] = cur
        cur += 1
        node.append((x, y))
        
  nodes = [Node(i)for i in range(cur)]
  for x, y in node:
    z = idx[x][y]
    
    for u, v in direction:
      k = 0
      while True:
        k += 1
        xd = x+u*k
        yd = y+v*k
        
        path = m.get(xd, yd)
        if path in [Maze.Wall, None]: break
        res = idx[xd][yd]
        if res == -1: continue
        nodes[z].path.append((nodes[res], k))
        break
  
  sol = findPath(nodes, cur, info)
  res = ''
  first, *path = sol
  prev_x, prev_y = node[first]
  for i in path:
    cur_x, cur_y = node[i]
    if prev_x == cur_x:
      c = cur_y - prev_y
      d = 'LR'
    else:
      c = cur_x - prev_x
      d = 'UD'
    res += d[c > 0]*abs(c)
    prev_x, prev_y = cur_x, cur_y

  return res

def solution(maze, start):
  *sol, _ = findMaze(maze)
  res = list(map(list, maze.split('\n')))
  x, y = start
  for i in sol:
    if i == 'R': x += 1
    if i == 'L': x -= 1
    if i == 'U': y -= 1
    if i == 'D': y += 1
    res[y][x] = '::'
  return '\n'.join(map(lambda x: ''.join(x), res))

def main():
  maze = """
000000000000000000000000000000000
+~~~~~~~0~~~~~~~~~0~~~0~~~~~0~~~0
0~00000~0~0~00000~0~0~000~0~0~0~0
0~~~0~~~0~0~0~~~~~~~0~~~~~0~~~0~0
0~000~000~0~0000000000000000000~0
0~~~0~0~~~0~~~~~~~0~~~0~~~~~~~0~0
0~0~0~0~00000~000~0~0~0~00000~0~0
0~0~0~0~0~~~0~~~0~0~0~0~0~0~~~0~0
000~0~000~0~00000~0~0~0~0~0~000~0
0~~~0~~~0~0~0~~~~~0~0~~~0~0~~~~~0
0~00000~0~0~0~00000~00000~0000000
0~~~~~0~~~0~~~0~~~0~~~0~~~~~~~~~0
0~0~00000000000~0~000~0~0000000~0
0~0~~~0~~~~~~~~~0~~~0~~~0~~~~~0~0
0~000~0~00000000000~00000~00000~0
0~0~0~0~~~0~~~0~~~~~~~~~0~~~~~~~0
0~0~0~0~000~0~0~0000000~0~0000000
0~~~0~~~0~~~0~~~0~~~~~0~0~~~0~~~0
000~00000~0000000~00000~000~0~000
0~~~0~~~~~0~~~~~~~0~~~~~0~0~0~~~0
00000~00000~000~000~00000~0~0~0~0
0~~~0~0~0~~~0~0~~~~~0~~~~~0~0~0~0
0~0~0~0~0~000~0000000~000~0~000~0
0~0~~~0~~~~~~~~~~~~~~~0~~~0~~~0~0
0~0~00000000000~0000000000000~0~0
0~0~0~~~0~~~~~~~0~~~~~~~~~0~~~0~0
0~000~0~0~0000000~0000000~0~000~0
0~~~~~0~0~~~0~~~~~0~~~~~0~0~0~~~0
0~00000~000~0~00000~00000~0~0~0~0
0~0~~~0~~~0~0~~~~~0~0~~~~~0~0~0~0
0~000~000~0000000~0~0~00000~0~0~0
0~~~~~~~0~~~~~~~~~~~0~~~~~~~~~0~=
000000000000000000000000000000000
  """.strip()

  print(maze)
  print()
  print(solution(maze, (0, 1)))
  print()
  print(findMaze(maze))

if __name__ == '__main__': main()
