from typing import List, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:


        length_of_the_array = len(nums)

        # Exit conditions
        if length_of_the_array == 1:
            return TreeNode(nums[0])
        elif length_of_the_array == 0:
            return None

        # find the middle element
        mid_point = length_of_the_array//2
        # print(f"mid_point {mid_point} length_of_the_array {length_of_the_array}")
        root = TreeNode(nums[mid_point])
        # insert to the left
        root.left = self.sortedArrayToBST(nums[0:mid_point])

        # print(root)

        root.right = self.sortedArrayToBST(nums[mid_point+1:length_of_the_array])

        # print(root)
        return root

