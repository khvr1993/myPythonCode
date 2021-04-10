from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        """
        if not(nums):
            return 0
        i = 0
        for j in range(1,len(nums)):
            # if first value is not equal to second value then
            # increment the pointer of i.
            # What we are doing to moving all the elements left
            """
            for eg: consider [1,2,3,3,4]
                for 1,2,3 its regular operation
                when j = 3 [ i = 2]
                i skips incrementing
                when j = 4 [ i = 2]
                i increments and holds value of j =4 at 3


            """
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        # print(nums)
        return i + 1

pbm = Solution()
nums = [1,1,2]
op = pbm.removeDuplicates(nums)
print(op)