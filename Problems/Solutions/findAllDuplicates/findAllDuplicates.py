from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      """
      Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

      Find all the elements that appear twice in this array.

      Could you do it without extra space and in O(n) runtime?

      Solution:
        This is a trick problem
        since the array is of size n and also the elements stay between size n
        to find the duplicates we need to loop through the array
        for every element
        1. take the element subtract is by -1 and multiple a[element-1]*-1
        2. Before multiplying => If a[element-1] < 0 then the current element is duplicate and
          skip the multiplication.

      """
      op = []

      for item in nums:
        index = abs(item)-1
        if nums[index] < 0:
          op.append(abs(item))
        else:
          nums[index] *= -1

      return op


