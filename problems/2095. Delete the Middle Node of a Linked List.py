"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""

#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        fast = head.next.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head