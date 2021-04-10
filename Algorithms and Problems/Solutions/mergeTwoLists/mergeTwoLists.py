from typing import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        https://leetcode.com/problems/merge-two-sorted-lists/
        Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
        """
        head = ListNode();
        curr_node = head

        if not(l1) and not(l2):
            return None

        while l1 and l2:
            # print("-----------")
            # print(f"l1 is {l1}")
            # print(f"l2 is {l2}")
            # print(f"head {head}")

            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next

        if l1 :
            curr_node.next = l1
            l1.next
            curr_node = curr_node.next

        if l2:
            curr_node.next = l2
            l2.next
            curr_node = curr_node.next

        # print(head)
        return head.next





