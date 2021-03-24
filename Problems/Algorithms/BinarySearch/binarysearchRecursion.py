from typing import List
class Solution:
  def search(self,arr,low,high,search_element) -> bool :
    """
      Implements search recursively
    """
    if low <= high :
      mid = low + (high-low)//2
      print(f"low = {low} high = {high} mid = {mid}")
      if arr[mid] == search_element:
        return True
      elif arr[mid] < search_element:
        return self.search(arr,mid+1,high,search_element)
      elif arr[mid] > search_element:
        return self.search(arr,low,mid-1,search_element)
    return False



  def binarySearch(self,arr : List[int],search_element : int) -> bool:
    """
    Implements binary Search.
    Prerequisite is the list should be sorted.
    I am using pythons sorted method because built in sort method
    is almost 10 times faster than the QuickSort or MergeSort.
    Using extra O(n) space
    """

    sorted_list = sorted(arr)
    print(sorted_list)

    low = 0
    high = len(arr)

    index_of_search = self.search(sorted_list,low,high,search_element)

    return index_of_search


pbm =  Solution()
arr = [5,8,3,4,1,0,8]
op = pbm.binarySearch(arr,5)
print(op)