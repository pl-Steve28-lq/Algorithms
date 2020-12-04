class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0
  
  def appendLast(self, node):
    if not self.head: self.head = node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = node
    self.length += 1
  
  def appendByIndex(self, idx, node):
    newidx = 0
    cur = self.head
    while newidx != idx-1:
      cur = cur.next
      newidx += 1
    node.next = cur.next
    cur.next = node
    self.length += 1
  
  def findIndexByValue(self, data):
    cur = self.head
    idx = 0
    while cur:
      if cur.data = data: return idx
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
    cur = self.head
    res = ""
    while cur:
      res += f"{cur.data}{' -> ' if cur.next else ''}"
      cur = cur.next
    print(res)
