from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and Conquer Approach
        divide the array at mid.
        find the best sum at the left array
        find the best sum in the right array
        find the best sum including the mid

        https://leetcode.com/problems/maximum-subarray/solution/
        Watch the animation for the maximum sum including both the arrays

        """
        def findMaxSubArray(nums,left,right) -> int:
            print("===================")
            print(f"Args : left - {left} {right}")

            # exit condition
            if left > right :
                return -math.inf

            # calculate the mid point
            mid = (left+right)//2
            print(f"mid - {mid}")

            current_sum = 0
            best_right_sum = 0
            best_left_sum = 0

            # Calculating the sum of all the elements in the left subarray
            # Here we are going from mid to left because we want to include the mid and see
            # at the end what is the maximum possible value
            for i in range(mid-1,left-1,-1):
                current_sum += nums[i]
                best_left_sum = max(best_left_sum,current_sum)

            current_sum = 0
            # Calculating the sum of all the elements in the right subarray
            for i in range(mid+1,right+1,1):
                current_sum += nums[i]
                best_right_sum = max(best_right_sum,current_sum)

            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            print(f"best_left_sum = {best_left_sum} best_right_sum = {best_right_sum} nums[mid] = {nums[mid]} best_combined_sum = {best_combined_sum}")

            left_half = findMaxSubArray(nums,left,mid-1)
            right_half = findMaxSubArray(nums,mid+1,right)

            print(f"left_half = {left_half} right_half = {right_half} best_combined_sum = {best_combined_sum}")

            return max(best_combined_sum,left_half,right_half)
        return findMaxSubArray(nums,0,len(nums)-1)

pbm = Solution()
nums = [5,-2,1,-3,4,-2,1]
# nums = [-5,-2,-1,-20,-4,-2,-1]
op = pbm.maxSubArray(nums)
print(op)


