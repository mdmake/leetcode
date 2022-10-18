"""
link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

solution: https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tortoise = head
        hare = head

        while tortoise:
            try:
                tortoise = tortoise.next
                hare = hare.next.next

                if tortoise == hare:
                    return True
            except:
                return False

        return False
