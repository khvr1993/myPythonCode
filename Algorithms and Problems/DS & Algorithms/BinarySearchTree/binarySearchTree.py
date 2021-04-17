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

    def put (self,key,value):
        if self.root == None:
            self.root = Node(key, value)
            return
        else :
            self.__put(self.root,key,value)

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

    def height(self,node: Node) -> int:
        """
        This process tells you the height of the tree from that particular Node
        """
        if node == None:
            height = self.__height(self.root)
        else :
            height = self.__height(node)

        return height

    def bft(self,node: Node):
        """
        Breadth First Traversal
        Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
        It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]),
        and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

        https://www.geeksforgeeks.org/level-order-tree-traversal/

        """
        self.__print_level_order(node)
        print("")

    def inorder_traversal(self):
        """
        For a tree with root 1 ; left node 2 and right node 3
                    1
                2       3
            4       5

        the Depth First Traversals of this Tree will be:
        (a) Inorder   (Left, Root, Right) : 4 2 5 1 3
        (b) Preorder  (Root, Left, Right) : 1 2 4 5 3
        (c) Postorder (Left, Right, Root) : 4 5 2 3 1
        """
        self.__inorder_traversal(self.root)
        print("")

    def preorder_traversal(self):
        """
        For a tree with root 1 ; left node 2 and right node 3
                    1
                2       3
            4       5

        the Depth First Traversals of this Tree will be:
        (a) Inorder   (Left, Root, Right) : 4 2 5 1 3
        (b) Preorder  (Root, Left, Right) : 1 2 4 5 3
        (c) Postorder (Left, Right, Root) : 4 5 2 3 1
        """
        self.__preorder_traversal(self.root)
        print("")

    def postorder_traversal(self):
        """
        For a tree with root 1 ; left node 2 and right node 3
                    1
                2       3
            4       5

        the Depth First Traversals of this Tree will be:
        (a) Inorder   (Left, Root, Right) : 4 2 5 1 3
        (b) Preorder  (Root, Left, Right) : 1 2 4 5 3
        (c) Postorder (Left, Right, Root) : 4 5 2 3 1
        """
        self.__postorder_traversal(self.root)
        print("")


    def __put(self, node, key, value):
        """
        Inserts the node into the right place
        """
        # print(f"===================")
        # print(f"node => {node}")
        # print(f"Key being inserted : {key} Value is {value} ")

        if self.root == None:
            self.root = Node(key, value)
            return

        if node == None:
            return Node(key, value)

        print(f"{node.key > key}")

        if node.key > key:
            node.left_node = self.__put(node.left_node, key, value)
        elif node.key < key:
            node.right_node = self.__put(node.right_node, key, value)
        else:
            node.value = value
            node.key = key

        node.size = 1 + self.__size(node.left_node) + self.__size(node.right_node)

        # print(f"===================")
        return node

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

    def __size(self, node):
        if node == None:
            return 0
        else:
            return node.size

    def __deleteMin(self, x):
        if x.left_node == None:
            return x.right_node
        else:
            x.left_node = self.__deleteMin(x.left_node)

        x.size = 1 + self.__size(x.left_node) + self.__size(x.right_node)

        return x

    def __height(self,node) -> int:
        if node == None:
            return 0
        else:
            # Here we first calculate the left side hieght and right side height and return the value
            left_height = self.__height(node.left_node)
            right_height = self.__height(node.right_node)

        if left_height > right_height:
            return 1 + left_height # Adding one to include the root node value
        else :
            return 1 + right_height

    def __print_level_order(self,node):
        """
        From the given node print all the levels
        """
        height = self.height(node)
        for i in range(1,height+1):
            # From the given node level we go and print its following elements
            # node,node.left,node.right
            # node.left.left,node.left.right ; node.right.left,node.right.right ...
            self.__print_given_level(node,i)

    def __print_given_level(self,node,level,append = ""):
        """
        Prints the nodes at the given level using recursive approach
        """
        #Reached the end
        if append == "":
            append = "R"
        if node == None:
            return

        # Reached the desired level after recursion
        if level == 1:
            print(append+"-"+str(node.key),end = '  ')
        elif level > 1 :
            # As level decreases we go to the next level of the binary search tree
            # Print the left side Node
            self.__print_given_level(node.left_node,level-1,'L')
            # Print the right side node
            self.__print_given_level(node.right_node,level-1,'R')

    def __inorder_traversal(self,node: Node):
        """
            Inorder traversal private method
        """
        if node:
            self.__inorder_traversal(node.left_node)
            print(node.key, end = " ")
            self.__inorder_traversal(node.right_node)

    def __preorder_traversal(self,node: Node):
        """
            Preorder Traversal
        """
        if node :
            print(node.key, end = " ")
            self.__inorder_traversal(node.left_node)
            self.__inorder_traversal(node.right_node)

    def __postorder_traversal(self,node:Node):
        """
            Postorder Traversal
        """
        if node:
            self.__inorder_traversal(node.left_node)
            self.__inorder_traversal(node.right_node)
            print(node.key,end =" ")

s = binarySearchTree()
s.put(50, "a")
s.put(100, "b")
s.put( 40, "c")
s.put(60, "d")
s.put(110, "e")
print(f"Size {s.size()}")
print(f"delete Min {s.deleteMin()}")
print(f"Size {s.size()}")
s.put(40, "f")
s.put(120,"g")
s.put(10,"h")
s.put(20,"i")
s.put(130,"j")

print(f"root {s.root} ")
print(f"Left Node {s.root.left_node}")
print(f"Right Node {s.root.right_node.left_node}")
print(f"Right Node {s.root.right_node.right_node}")
print(f"Floor of 70 is {s.floor(70)}")
print(f"Height of the tree is {s.height(None)}")
s.bft(s.root)
s.inorder_traversal()
s.preorder_traversal()
s.postorder_traversal()
