from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/squares-of-a-sorted-array/

        Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
        """
        print(f"nums {nums}")
        point_of_inversion = -1
        positive_found = False

        if nums[0] >= 0:
            point_of_inversion = -1
            positive_found = True
        else:
            for i in range(len(nums)):
                if nums[i] >= 0 :
                    point_of_inversion = i
                    positive_found = True
                    break

        if point_of_inversion == -1 and positive_found:
            return list(map(lambda x : x*x, nums))
        elif point_of_inversion == -1 and not(positive_found):
            return list(reversed(list(map(lambda x : x*x, nums))))

        print(f"point_of_inversion {point_of_inversion}")
        result = []

        i = point_of_inversion - 1
        j = point_of_inversion
        k = 0
        while i >= 0 and j < len(nums):
            square1 = nums[i]*nums[i]
            square2 = nums[j]*nums[j]
            if square1 < square2:
                result.append(square1)
                i -= 1
            else:
                result.append(square2)
                j += 1

        while i >= 0:
            square1 = nums[i]*nums[i]
            result.append(square1)
            i -= 1
        while j < len(nums):
            square2 = nums[j]*nums[j]
            result.append(square2)
            j += 1

        return result

pbm = Solution()
nums = [0,2]
op = pbm.sortedSquares(nums)
print(op)

