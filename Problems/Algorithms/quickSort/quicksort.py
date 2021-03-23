from typing import List

class Solution:
  def quickSort(self,arr : List[int],low,high) -> List[int]:
    """
      Quick Sort follows DIVIDE and Conquer
      O(nlogn) Worst case O[n2]

      1. We have to choose a pivot element.
      2. All the elements less than pivot are to be placed in the left hand side
      3. All the elements to the right are to be placed in the right hand side
    """

    def swap(i,j):
      """swaps the elements
        jth position element will move to ith position
      """
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp


    def partition(low,high) -> int :
      """
      Implements parition for quick sort
      """
      pivot = arr[high-1]

      print(f"pivot = {pivot} low = {low} high = {high}")

      i = low-1 # starting point

      # for the array items check if the element is less than the pivot element
      # the element should be placed in the left hand side
      # If the element is greater then it should be moved to right
      for j in range(low,high):
        if arr[j] < pivot:
          i += 1
          # swap the element to the left
          # When element is greater the swap is skipped and i is not incremented.
          # What this does is for any element after this element the swap happens
          swap(i,j)
          print(arr)


      swap(i+1,j) # Final Swap

      return (i+1)

    if (low < high):
      pi = partition(low,high)

      self.quickSort(arr, low, pi-1)
      self.quickSort(arr, pi+1, high)

    return arr



pbm = Solution()
arr = [10, 80, 30, 90, 40, 50, 70]
op = pbm.quickSort(arr,0,len(arr))
print(op)



