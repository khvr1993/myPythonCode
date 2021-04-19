from typing import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        https://leetcode.com/problems/balanced-binary-tree/

        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:

        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
        """
        def height_of_node(node: TreeNode) -> int:
            if not(node):
                return 0
            else:
                return 1 + max(height_of_node(node.left),height_of_node(node.right))

        if root == None:
            return True

        height_of_left_node = height_of_node(root.left)
        height_of_right_node = height_of_node(root.right)



        if abs(height_of_left_node - height_of_right_node) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
