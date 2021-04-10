from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      """
      https://leetcode.com/problems/remove-element/
      Given an array nums and a value val, remove all instances of that value in-place and return the new length.

      Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
      """
      i = 0
      length_of_the_array = len(nums)
      while i < length_of_the_array:
          if (nums[i] == val):
              # copy the last element to the first position
              nums[i] = nums[length_of_the_array-1]
              # we need not look at last element now
              length_of_the_array -= 1
          else :
              i +=1
      return length_of_the_array
