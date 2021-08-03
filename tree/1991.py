class Node():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    pass

class Tree():
  def __init__(self):
    self.nodes = [None for i in range(26)]

  def insert(self, parent, left, right):
    node = None

    if self.nodes[ord(parent) - 65]:
      node = self.nodes[ord(parent) - 65]
    else:
      node = Node(parent)
      self.nodes[ord(parent) - 65] = node
    
    if left != ".":
      node.left = self.nodes[ord(left) - 65] if self.nodes[ord(left) - 65] else Node(left)
      self.nodes[ord(left) - 65] = node.left
    if right != ".":
      node.right = self.nodes[ord(right) - 65] if self.nodes[ord(right) - 65] else Node(right)
      self.nodes[ord(right) - 65] = node.right
    
  def preoder(self, curr: Node):
    print(curr.val, end="")
    if curr.left:
      self.preoder(curr.left)
    if curr.right:
      self.preoder(curr.right)

  def inorder(self, curr: Node):
    if curr.left:
      self.inorder(curr.left)
    print(curr.val, end="")
    if curr.right:
      self.inorder(curr.right)

  def postorder(self, curr: Node):
    if curr.left:
      self.postorder(curr.left)
    if curr.right:
      self.postorder(curr.right)
    print(curr.val, end="")



tree = Tree()

for i in range(int(input())):
  a, b, c = input().split()
  tree.insert(a, b, c)


tree.preoder(tree.nodes[0])
print()
tree.inorder(tree.nodes[0])
print()
tree.postorder(tree.nodes[0])