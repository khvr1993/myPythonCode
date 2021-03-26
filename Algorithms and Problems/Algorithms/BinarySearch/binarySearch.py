from typing import List
class Solution:
  def binarySearch(self,arr : List[int],search_element : int) -> int:
    """
    Implements binary Search.
    Prerequisite is the list should be sorted.
    I am using pythons sorted method because built in sort method
    is almost 10 times faster than the QuickSort or MergeSort.
    Using extra O(n) space
    """

    sorted_list = sorted(arr)
    print(sorted_list)

    length_of_array = len(sorted_list)

    low = 0
    high = length_of_array

    while low <= high:
      mid = low + (high-low)//2

      print(f"low = {low} high = {high} mid = {mid}")


      if sorted_list[mid] == search_element:
        return mid
      elif sorted_list[mid] > search_element:
        high = mid - 1
      elif sorted_list[mid] < search_element:
        low = mid + 1

    return -1

pbm =  Solution()
arr = [5,8,3,4,1,0,8]
op = pbm.binarySearch(arr,0)
print(op)



