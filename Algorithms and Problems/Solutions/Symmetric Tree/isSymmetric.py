from typing import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = []
        stack2 = []
        def build_stack(node: TreeNode,stack,traverse='LEFT') -> List[int]:
            if node == None:
                stack.append('-999')
                return
            # print(f"Entering build stack for node {node.val}")
            if traverse == 'LEFT':
                stack.append(node.val)
                build_stack(node.left,stack,traverse)
                build_stack(node.right,stack,traverse)
            else:
                stack.append(node.val)
                build_stack(node.right,stack,traverse)
                build_stack(node.left,stack,traverse)
            return

        if not(root.left) and not(root.right):
            return True
        elif not(root.left) or not(root.right):
            return False
        elif root.left.val != root.right.val:
            return False
        else:
            """
            stack method
            """
            build_stack(root.left,stack,'LEFT')
            build_stack(root.right,stack2,'RIGHT')
            # print(stack)
            # print(stack2)
            if stack == stack2:
                return True
