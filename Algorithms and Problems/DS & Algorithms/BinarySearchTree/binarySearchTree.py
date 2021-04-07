"""
Class of Node
"""


class Node:
    """
    Here we are defining a node object which containts attributes
    key,value,link to left node, link to right Node
    """

    # Constructor method for the binary search tree Node
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_node = None
        self.right_node = None
        self.size = 1

    def __repr__(self):
        return "Node( Key : " + str(self.key) + " value : " + str(self.value) + ")"


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

    def put(self, root, key, value):
        """
        Inserts the node into the right place
        """
        print(f"===================")
        print(f"Root => {root}")
        print(f"Key being inserted : {key} Value is {value} ")

        if self.root == None:
            self.root = Node(key, value)
            return

        if root == None:
            return Node(key, value)

        print(f"{root.key > key}")

        if root.key > key:
            root.left_node = self.put(root.left_node, key, value)
        elif root.key < key:
            root.right_node = self.put(root.right_node, key, value)
        else:
            root.value = value
            root.key = key

        root.size = 1 + self.__size(root.left_node) + self.__size(root.right_node)

        print(f"===================")
        return root

    def __floor(self, root, key):
        if root == None:
            return None
        elif key < root.key:
            return self.__floor(root.left_node, key)
        elif key == root.key:
            return root
        else:
            t = self.__floor(root.right_node, key)
            if t != None:
                return t
            else:
                return root

    def floor(self, key):
        """
        returns the floor
        """
        return self.__floor(self.root, key)

    def size(self):
        """
        returns the size of the BST
        """
        s = self.__size(self.root)
        return s

    def __size(self, root):
        if root == None:
            return 0
        else:
            return root.size

    def deleteMin(self):
        """
        Deletes the minimum value in a binary tree
        1. return the node which is just greater than the minimum
        2. We have to go left till we are left with a null link
        3. Replace that node with its right link
        4. Update subtree counts
        """
        root = self.__deleteMin(self.root)
        print(root)

    def __deleteMin(self, x):
        if x.left_node == None:
            return x.right_node
        else:
            x.left_node = self.__deleteMin(x.left_node)

        x.size = 1 + self.__size(x.left_node) + self.__size(x.right_node)

        return x



s = binarySearchTree()
s.root = Node(50, "x")
s.put(s.root, 100, "y")
s.put(s.root, 40, "z")
s.put(s.root, 60, "a")
s.put(s.root, 110, "a")
print(f"Size {s.size()}")
print(f"delete Min {s.deleteMin()}")
print(f"Size {s.size()}")

print(f"root {s.root} ")
print(f"Left Node {s.root.left_node}")
print(f"Right Node {s.root.right_node.left_node}")
print(f"Right Node {s.root.right_node.right_node}")
print(f"Floor of 70 is {s.floor(70)}")
