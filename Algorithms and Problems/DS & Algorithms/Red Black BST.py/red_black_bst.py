
RED = True
BLACK = False
class Node:
    def __init__(self,key,value,color = RED):
        self.key = key
        self.value = value
        self.left_node = None
        self.right_node = None
        self.color = color
        self.size = 1

    @staticmethod
    def isRed(x):
            """
            Returns whether the provided node is Red or Not
            """
            if x == None:
                return False
            return x.color == RED


class red_black_tree:
    """
    Implements red black BST

    Properties:
    1. Red Links Lean Left
    2. No Node has 2 red links connected to it
    3. The tree has perfect Black Balance. Every path from the root to a null link has the same number of black links
    """
    def __init__(self):
        self.root = None

    def __size(self,x: Node):
        """
        Returns the size of the Node
        """
        if x == None:
            return 0
        else :
            return x.size

    def size(self,x):
        s = self.__size(x)
        return s

    def rotateLeft(self,h: Node):
        """
        Converts a right leaning red black BST (RED link present to the right) to a left leaning red black BST
        1. Copy the right link to a temp variable
        2. make temps left link to the right link of root
        2. Make the temp variable root
        3. temp.left will be the previous root
        """
        print(f"rotateLeft at {h.key}")
        temp = h.right_node
        h.right_node = temp.left_node
        temp.left_node = h
        temp.color = h.color
        h.color = RED # Making this a red Node[Left side]
        temp.size = h.size # Size remains same since we just shifted root and we have to assign the correct size
        h.size = 1 + self.size(h.left_node)+ self.size(h.right_node)

        return temp

    def rotateRight(self,h: Node):
        """
        Converts a left leaning red black BST to right leaning red black BST
        """
        print(f"rotateRight at {h.key}")
        temp = h.left_node
        h.left_node = temp.right_node
        temp.right_node = h
        temp.color = h.color
        h.color = RED
        temp.size = h.size
        h.size = 1 + self.size(h.left_node)+ self.size(h.right_node)

        return temp

    def put(self,key,value):
        """
        Search for the key sent.
        If found then update the value
        Else add a node
        """
        print(f"BEGIN = Put key => {key}")
        self.root = self.__put(self.root,key,value)
        self.root.color = BLACK

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

    def __flipColors(self,h: Node):
        """
        Flips the colors of the node
        """
        print(f"Flip Colors")
        h.color = RED
        h.left_node.color = BLACK
        h.right_node.color = BLACK

    def __put(self,node: Node,key,value) -> Node:
        """
        Inserts the node in a red_black_tree
        """
        if node == None:
            return Node(key,value,RED)

        if  key < node.key :
            node.left_node = self.__put(node.left_node,key,value)
        elif key > node.key:
            node.right_node = self.__put(node.right_node,key,value)
        else:
            node.value = value

        # Right Node is red and left node is not red
        if Node.isRed(node.right_node) and not(Node.isRed(node.left_node)):
            node = self.rotateLeft(node)
        # On the left side 2 red nodes are contiguos
        if Node.isRed(node.left_node) and Node.isRed(node.left_node.left_node):
            node = self.rotateRight(node)
        # left and right nodes are red
        if Node.isRed(node.left_node) and Node.isRed(node.right_node):
            self.__flipColors(node)

        node.size = 1 + self.size(node.left_node)+ self.size(node.right_node)

        return node

    def __inorder_traversal(self,node: Node):
        """
            Inorder traversal private method
        """
        if node:
            self.__inorder_traversal(node.left_node)
            color = 'RED' if node.color else 'BLACK'
            print(str(node.key)+"-"+color, end = " ")
            self.__inorder_traversal(node.right_node)

    def __preorder_traversal(self,node: Node):
        """
            Preorder Traversal
        """
        if node :
            color = 'RED' if node.color else 'BLACK'
            print(color+"-"+str(node.key), end = " ")
            self.__inorder_traversal(node.left_node)
            self.__inorder_traversal(node.right_node)

    def __postorder_traversal(self,node:Node):
        """
            Postorder Traversal
        """
        if node:
            self.__inorder_traversal(node.left_node)
            self.__inorder_traversal(node.right_node)
            color = 'RED' if node.color else 'BLACK'
            print(str(node.key)+"-"+color, end = " ")


bst = red_black_tree()
bst.put("S",1)
bst.put("E",1)
bst.put("A",1)
bst.put("R",1)
bst.put("C",1)
bst.put("H",1)
bst.put("E",1)
bst.put("X",1)
bst.put("A",1)
bst.put("M",1)
bst.put("P",1)
bst.put("L",1)
bst.put("E",1)
print(bst.root.value)
bst.inorder_traversal()


