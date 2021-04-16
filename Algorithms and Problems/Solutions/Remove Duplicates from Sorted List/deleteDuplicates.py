from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        https://leetcode.com/problems/remove-duplicates-from-sorted-list/

        Given the head of a sorted linked list,
        delete all duplicates such that each element appears only once.
        Return the linked list sorted as well.
        """
        # No elements

        if head == None:
            return None

        # Only 1 element
        if head.next == None:
            return head

        Head_node = head
        current_val = head.next
        previous_val = head

        # print(f"Head_node[previous val] {Head_node.val} current_val {current_val.val}")

        while current_val :
            # print(f"previous_val {previous_val.val} current_val {current_val.val}")
            if previous_val.val == current_val.val:
                #break the node
                temp_node = current_val.next
                previous_val.next = temp_node
                current_val = temp_node
            else:
                current_val = current_val.next
                previous_val = previous_val.next

        return Head_node

