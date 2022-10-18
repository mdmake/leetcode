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

        curNode1 = list1
        curNode2 = list2

        if list1 is None:
            if list2 is None:
                return None
            else:
                return list2
        elif list2 is None:
            if list1 is None:
                return None
            else:
                return list1

        if curNode1.val < curNode2.val:
            result = ListNode(curNode1.val)
            curNode1 = curNode1.next
        else:
            result = ListNode(curNode2.val)
            curNode2 = curNode2.next

        currentState = (curNode1 is not None) and (curNode2 is not None)

        result_cn = result
        while currentState:

            if curNode1.val < curNode2.val:
                result_cn.next = ListNode(curNode1.val)
                curNode1 = curNode1.next
            else:
                result_cn.next = ListNode(curNode2.val)
                curNode2 = curNode2.next

            result_cn = result_cn.next

            currentState = (curNode1 is not None) and (curNode2 is not None)

        if curNode1 is None:
            result_cn.next = curNode2
        else:
            result_cn.next = curNode1

        return result


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    t = Solution()

    rez = t.mergeTwoLists(list1, list2)

    a = 2
