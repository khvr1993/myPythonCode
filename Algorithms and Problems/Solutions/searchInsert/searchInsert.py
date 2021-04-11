from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-insert-position/

        Using Binary Search to find the optimum position since array is sorted
        """
        # Handle Overflow cases
        if target > max(nums):
          return len(nums)
        if target < min(nums):
          return 0
        else:
          return self.BinarySearch(nums,0,len(nums),target)

    def BinarySearch(self,nums,low,high,target):
      while low < high :
        mid = low + (high-low)//2
        print(f"mid => {mid} low => {low} high => {high}")

        if nums[mid] == target:
          return mid
        elif nums[mid] < target:
          # Search on right
          return self.BinarySearch(nums,mid+1,high,target)
        else:
          return self.BinarySearch(nums,low,mid-1,target)

      # Search element not found. Insert it in a place where the position is right
      return high+1 if target > nums[high] else high

pbm = Solution()
nums = [1,3,5,6]
target = 5
op = pbm.searchInsert(nums,target)
print(op)
