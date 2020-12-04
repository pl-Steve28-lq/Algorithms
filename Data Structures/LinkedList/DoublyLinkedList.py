class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.length = 0

  def isEmpty(self):
    return self.head.next == self.tail

  def appendLast(self, node):
    if self.isEmpty():
      self.head.next = node
      self.tail.prev = node
      node.next = self.tail
      node.prev = self.head
    else:
      node.prev = self.tail.prev
      node.next = self.tail
      self.tail.prev.next = node
      self.tail.prev = node
    self.length += 1

  def appendFirst(self, node):
    if self.isEmpty():
      self.head.next = node
      self.tail.prev = node
      node.next = self.tail
      node.prev = self.head
    else:
      node.prev = self.head
      node.next = self.head.next
      self.head.next.prev = node
      self.head.next = node
    self.length += 1

  def appendByIndex(self, idx, node):
    if idx == 0: self.appendFirst(node)
    elif idx == self.length: self.appendLast(node)
    else:
      left = idx < self.length//2
      newidx = 0 if left else self.length
      cur = self.head if left else self.tail
      pluser = 1 if left else -1
      while newidx != idx - pluser:
        cur = cur.next if left else cur.prev
        newidx += pluser
      if left:
        node.next = cur
        cur.prev.next = node
        cur.prev = node
      else:
        node.prev = cur
        cur.next.prev = node
        cur.next = node
      self.length += 1

  def findIndexByValue(self, data):
    cur = self.head.next
    idx = 0
    while cur != self.tail:
      if cur.data == data: return idx
      cur = cur.next
      idx += 1
    return -1

  def findNodeByIndex(self, idx):
    if idx == self.length: return self.tail.prev
    if idx == 0: return self.head.next
    left = idx < self.length//2
    newidx = 0 if left else self.length
    cur = self.head.next if left else self.tail.prev
    pluser = 1 if left else -1
    while newidx != idx - pluser:
      cur = cur.next if left else cur.prev
      newidx += pluser
    return cur

  def print(self):
    cur = self.head.next
    res = ""
    while cur.next:
      res += f"{cur.data}{' <-> ' if cur.next != self.tail else ''}"
      cur = cur.next
    print(res)
