from typing import List

class Node:
  """
    The Node class contains 2 attributes
    value
    and link to the next node.
    On initialization the value is set and the next node is by default set to None
  """
  def __init__(self,val) -> None:
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


  def insertNode(self,val):
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
    else :
      temp = self.head.next
      ret_val = self.head.val
      self.head = temp
      print(f"Popped NodeVal is {ret_val}")
      return ret_val

  def print_list(self):
    li = self.head
    while li :
      print(li.val)
      li = li.next


s_list = LinkedList()
s_list.insertNode(4)
s_list.insertNode(5)
s_list.insertNode(6)
s_list.insertNode(47)
s_list.insertNode(815)

s_list.print_list()

s_list.pop_node()
s_list.print_list()













