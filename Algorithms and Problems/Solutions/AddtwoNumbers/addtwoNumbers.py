from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        https://leetcode.com/problems/add-two-numbers/

        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
         Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """

        carry = 0
        headNode = ListNode(0)
        sum_node = headNode
        node = None
        while l1 or l2 :

            if l1 == None and l2:
                l1 = ListNode(0)
            if l1 and l2 == None:
                l2 = ListNode(0)

            sum_val = l1.val+l2.val + carry
            carry = 0
            if sum_val > 9 :
                carry = 1
                sum_val = sum_val%10

            node = ListNode(sum_val)
            sum_node.next = node
            sum_node = sum_node.next

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
        if carry > 0 :
            sum_node.next = ListNode(carry)
        return headNode.next


