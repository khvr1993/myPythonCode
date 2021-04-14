from typing import List


class Node:
    """
    The Node class contains 2 attributes
    value
    and link to the next node.
    On initialization the value is set and the next node is by default set to None
    """

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        print(f"List {self.val} Next Node {self.next}")


class LinkedList:
    """
    Singly linked list.every node contains the value and the reference to the next node
    """

    def __init__(self) -> None:
        self.head = None

    def insertNode(self, val):
        """
        Inserts node at the head
        """
        if self.head == None:
            self.head = Node(val)
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp

    def pop_node(self):
        """
        Pops the first element out of the list
        """
        if self.head == None:
            print("No Node present in the list to pop")
        else:
            temp = self.head.next
            ret_val = self.head.val
            self.head = temp
            print(f"Popped NodeVal is {ret_val}")
            return ret_val

    def print_list(self,node : Node):
        if node:
            li=node
        else:
            li = self.head
        while li:
            print(str(li.val) + " --> ", end=" ")
            li = li.next
        print("")


    def reverseList(self):
        """
        Reverse a linked List
        """
        current = self.head
        reversed_list = None
        # loop through the list
        """
        Consider
        815 -->  47 -->  6 -->  5 -->  4 -->
        head = 815
        -------------------------
        first iteration
        next = 47{current.next}
        current = 815 _{head}
        current.next = reversed_list {in this case it becomes None}
        reversed_list = 815 {current}
        current = 47 {iterator}
        -------------------------
        second iteration
        next = 6
        current = 47
        current.next = 815
        reversed_list = 47
        current = 6

        """
        while current:
            # Copied the current node's next value into a temp var
            temp_node = current.next

            # Making it attach to the previous node
            # In this transaction we have assigned the previous iteration value to the current.next
            current.next = reversed_list

            # copy the current node to previous
            # In this transaction we have essentially reversed 2 elements
            # As we go further in the iteration we keep on moving the values by assigning
            reversed_list = current
            # Move the pointer forward
            current = temp_node
            self.print_list(reversed_list)
            # self.print_list(current)
        self.head = reversed_list






s_list = LinkedList()
s_list.insertNode(4)
s_list.insertNode(5)
s_list.insertNode(6)
s_list.insertNode(47)
s_list.insertNode(815)
s_list.print_list(None)

s_list.reverseList()
# s_list.print_list()

# s_list.pop_node()
s_list.print_list(None)
