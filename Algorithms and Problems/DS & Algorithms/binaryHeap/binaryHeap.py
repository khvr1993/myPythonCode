
from typing import List

class BinaryHeap:
  """
  This is an implementation of Binary Heap.
  The root node will always be maximum element. If an array is passed then the array will be arranged to gice a max binary heap

  """
  def __init__(self,arr: List):
    self.binaryHeap = arr
    self.parent_nodes = len(arr)//2
    self.size_of_heap = len(arr)

    self.construct_binary_heap()

  def __repr__(self):
    rep = 'BinaryHeap'+'('+"".join(str(self.binaryHeap)) + ' ParentNodes '+ str(self.parent_nodes)+')'
    return rep

  def construct_binary_heap(self):
    for i in reversed(range(1,self.parent_nodes+1)):
      print(f"Working on parent Node located at {i}")
      self.sink(i)
    print(repr(self.binaryHeap))

  def less(self,i,j):

    # print(f"Args Passed for Compare for i = {i} and j = {j}")

    if i > self.size_of_heap or j > self.size_of_heap:
      return False

    # print(f"Args Passed for Compare for i = {i} is {self.binaryHeap[i-1]} for j= {j} is {self.binaryHeap[j-1]}")

    if self.binaryHeap[i-1] < self.binaryHeap[j-1]:
      return True
    return False

  def exchange(self,i,j):
    # print(f"Args Passed for Exchange i = {i} j= {j}")
    temp = self.binaryHeap[j-1]
    self.binaryHeap[j-1] = self.binaryHeap[i-1]
    self.binaryHeap[i-1] = temp
    print(f"After Exchange {self.binaryHeap}")

  def sink(self,i):
    while 2*i < self.size_of_heap:
      if not(self.less(2*i,2*i+1)) and self.less(i,2*i):
        self.exchange(i,2*i)
        i = 2*i
      elif self.less(2*i,2*i+1) and self.less(i,2*i +1):
        self.exchange(i,2*i+1)
        i = 2*i+1
      else :
        i = 2*i


  def del_max(self):
    """
      To delete the max exchange the root node with the last element and
      perform sink operation
    """
    print("In function del max")
    self.exchange(1,self.size_of_heap)
    maxelem = self.binaryHeap.pop()
    self.size_of_heap = len(self.binaryHeap)
    self.parent_nodes = len(self.binaryHeap)//2
    print(maxelem)
    self.construct_binary_heap()
    return maxelem

heap = BinaryHeap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])

print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())
print(heap.del_max())