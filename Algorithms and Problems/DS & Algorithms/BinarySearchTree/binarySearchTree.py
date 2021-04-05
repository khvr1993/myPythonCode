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
		self.root = None

	def put(self,root,key,value):
		"""
			Inserts the node into the right place
		"""
		print(f"===================")
		print(f"Root => {root}")
		print(f"Key being inserted : {key} Value is {value} ")

		if (self.root == None):
			self.root = Node(key,value)
			return

		if (root == None):
			return Node(key,value)

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

	def floor_node(self,root,key):
		if root == None:
			return None
		elif key < root.key :
			return self.floor_node(root.left_node,key)
		elif key == root.key :
			return root
		else:
			t = self.floor_node(root.right_node,key)
			if t != None :
				return t
			else:
				return root




	def floor(self,key):
		"""
		returns the floor
		"""
		return self.floor_node(self.root,key)


s = binarySearchTree()
s.root = Node(50,'x')
s.put(s.root,100,'y')
s.put(s.root,40,'z')
s.put(s.root,60,'a')
s.put(s.root,110,'a')

print(f"root {s.root} ")
print(f"Left Node {s.root.left_node}")
print(f"Right Node {s.root.right_node.left_node}")
print(f"Right Node {s.root.right_node.right_node}")

print(f"Floor of 70 is {s.floor(70)}")




