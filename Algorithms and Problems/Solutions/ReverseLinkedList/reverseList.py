from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        https://leetcode.com/problems/reverse-linked-list/
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
        if head == None:
            return None

        current = head
        reversed_list = None

        while current:
            # Store the link to next nodes
            temp = current.next
            # Break the link by pointing it to the reversed_list
            current.next = reversed_list

            # Assigning this will reverse the nodes
            # As we iterate furthor the list reversal increases
            reversed_list = current

            # to move to the next node
            current = temp
            # print(reversed_list)

        return reversed_list