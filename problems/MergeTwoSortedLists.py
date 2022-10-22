"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1

        curNode1 = list1
        curNode2 = list2
        head = ListNode()

        result = head
        currentState = True

        while currentState:

            if curNode1.val < curNode2.val:
                result.next = ListNode(curNode1.val)
                curNode1 = curNode1.next
            else:
                result.next = ListNode(curNode2.val)
                curNode2 = curNode2.next

            result = result.next

            currentState = curNode1 and curNode2

        if curNode1 is None:
            result.next = curNode2
        else:
            result.next = curNode1

        return head.next

    def printNode(self, node: Optional[ListNode]):
        cn = node
        while cn:
            print(cn.val)
            cn = cn.next


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    t = Solution()

    rez = t.mergeTwoLists(list1, list2)
    t.printNode(rez)
