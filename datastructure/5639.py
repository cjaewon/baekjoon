import sys

sys.setrecursionlimit(20_000)

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def setRoot(self, val):
    self.root = Node(val)
  
  def insert(self, val):
    if self.root == None:
      self.setRoot(val)
    else:
      self.insertNode(self.root, val)

  def insertNode(self, curr: Node, val):
    if val <= curr.val:
      if curr.left:
        self.insertNode(curr.left, val)
      else:
        curr.left = Node(val)
    else:
      if curr.right:
        self.insertNode(curr.right, val)
      else:
        curr.right = Node(val)

  def postover(self, curr: Node):
    if curr == None:
      return

    self.postover(curr.left)
    self.postover(curr.right)
    print(curr.val)


tree = BinarySearchTree()

while True:
  t = sys.stdin.readline()

  if t == "\n" or t == "":
    break

  tree.insert(int(t))

tree.postover(tree.root)