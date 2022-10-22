import math

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        l = 0

        while current:
            l += 1
            current = current.next

        l = math.floor(l / 2)

        current = head
        i = 0
        while i < l:
            i += 1
            current = current.next

        return current

    def middleNode_2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        if not slow.next:
            return head

        try:
            while fast:
                fast = fast.next.next
                slow = slow.next
        except:
            return slow

        return slow


    def middleNode_3(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow