from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
        Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

        Notice that you may not slant the container.

        Solution :
        Maintain 2 pointers one at the begining. One at the end.
        Whichever is the larger height will remain constant while the ssmaller one will
        move forward to evaluate if any height is present after the current which might
        increase the area. Continue till both the points are same
        """
        start = 0
        end = len(height) - 1
        print(f"start {start} end {end}")
        max_area = -2147483647
        while (start < end):

            if height[start] > height[end]:
                #move the end to the left
                max_area = max((end-start)*height[end],max_area)
                end -= 1
            else:
                # move the start right
                max_area = max((end-start)*height[start],max_area)
                start += 1
        return max_area

pbm = Solution()
height = [1,8,6,2,5,4,8,3,7]
op = pbm.maxArea(height=height)
print(op)
