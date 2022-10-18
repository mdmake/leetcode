"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        result = ListNode(head.val)
        current = head.next
        rez_head = result

        while current:
            if current.val != result.val:
                result.next = current
                result = result.next

            current = current.next
        result.next = None

        return rez_head
