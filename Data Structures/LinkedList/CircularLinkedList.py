class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.tail.next = self.head
    self.length = 0
  
  def appendLast(self, node):
    if not self.head.next: self.head.next = node
    else:
      cur = self.head.next
      while cur.next == self.tail:
        cur = cur.next
      node.next = self.tail
      cur.next = node
    self.length += 1
  
  def appendByIndex(self, idx, node):
    newidx = 0
    cur = self.head.next
    while newidx != idx-1:
      cur = cur.next
      newidx += 1
    node.next = cur.next
    cur.next = node
    self.length += 1
  
  def findIndexByValue(self, data):
    cur = self.head.next
    idx = 0
    while cur:
      if cur.data == data: return idx
      cur = cur.next
      idx += 1
    return -1
  
  def findNodeByIndex(self, idx):
    newidx = 0
    cur = self.head
    while newidx != idx:
      cur = cur.next
      newidx += 1
    return cur
  
  def print(self):
    cur = self.head.next
    res = ""
    while cur != self.tail:
      res += f"{cur.data}{' -> ' if cur.next != self.tail else ''}"
      cur = cur.next
    print(res)
  
  def printCycle(self, n):
    cycled = 0
    cur = self.head.next
    while cycled != n:
      if cur == self.tail: cycled += 1
      elif cur == self.head: pass
      else: print(f"{cur.data} -> ", end='')
      cur = cur.next
    print("...")
