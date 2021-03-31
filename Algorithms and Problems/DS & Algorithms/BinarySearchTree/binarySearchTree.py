class binarySearchTree:
  """
  https://www.geeksforgeeks.org/binary-search-tree-data-structure/

  Implements Binary Search tree using recursive method.

  Binary Search Tree is a node-based binary tree data structure which has the following properties:

    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.s
  """

  # Constructor method for the binary search tree
  def __init__(self):
    pass

  def put(self,root,key,value):
    """
      Inserts the node into the right place
    """
    print(f"===================")
    print(f"Root => {root}")
    print(f"Key being inserted : {key} Value is {value} ")

    if (root == None):
      return self.Node(key,value)

    print(f"{root.key > key}")
    if root.key > key:
      root.left_node = self.put(root.left_node,key,value)
    elif root.key < key:
      root.right_node = self.put(root.right_node,key,value)
    else :
      root.value = value
      root.key = key

    print(f"===================")
    return root




  """
  Class of Node
  """
  class Node:
    """
      Here we are defining a node object which containts attributes
      key,value,link to left node, link to right Node
    """

    # Constructor method for the binary search tree Node
    def __init__(self,key,value):
      self.key = key
      self.value = value
      self.left_node = None
      self.right_node = None

    def __repr__(self):
      return 'Node( Key : ' + str(self.key) + ' value : ' + str(self.value) + ')'


s = binarySearchTree()
s.root = s.Node(50,'x')
root = s.root
print(f"root {root} ")
s.put(root,100,'y')
s.put(root,40,'z')
s.put(root,60,'a')
s.put(root,110,'a')

print(root.left_node)
print(root.right_node.left_node)
print(root.right_node.right_node)




