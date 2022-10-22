# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = deque()
        tail = current = head

        while current:
            stack.append(current)
            current = current.next

        while tail:
            if tail.val == stack.pop().val:
                tail = tail.next
            else:
                return False

        return True

    def isPalindrome_nice(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next

        return True
