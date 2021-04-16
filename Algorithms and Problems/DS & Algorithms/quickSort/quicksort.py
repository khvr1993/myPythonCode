from typing import List
import random


def shuffle(arr : List[int]):
  """
    Shuffles the given array randomly
  """
  length_of_array = len(arr)-1
  for i in range(1,length_of_array):
    randIndex = random.randint(i-1,length_of_array)
    # print(f"randIndex {randIndex} i is {i}" )
    swap(arr,randIndex,i)
  print(arr)


def swap(arr,i,j):
  """swaps the elements
    jth position element will move to ith position
  """
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp


class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    #Shuffle the array initially to get the best case for Quick sort
    shuffle(nums)
    arr = self.quickSort(nums,0,len(nums)-1)
    return arr


  def quickSort(self,arr : List[int],low,high) -> List[int]:
    """
      Quick Sort follows DIVIDE and Conquer
      O(nlogn) Worst case O[n2]

      Shuffle the array initially to get the best case for Quick sort

      1. We have to choose a pivot element.
      2. All the elements less than pivot are to be placed in the left hand side
      3. All the elements to the right are to be placed in the right hand side
    """

    def partition(low,high) -> int :
      """
      Implements partition for quick sort
      """
      pivot = arr[high]

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
          swap(arr,i,j)
          print(arr)


      # In Final Swap we need to move the pivot element to the correct position
      swap(arr,i+1,high)
      print(arr)

      return (i+1)

    if (low < high):
      pi = partition(low,high)

      self.quickSort(arr, low, pi-1)
      self.quickSort(arr, pi+1, high)

    return arr



pbm = Solution()
arr = [10, 80, 30, 90, 40, 70, 70]
shuffle(arr)
op = pbm.sortArray(arr)
print(op)



