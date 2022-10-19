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
