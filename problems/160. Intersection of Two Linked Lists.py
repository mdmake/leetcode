# Definition for singly-linked list.
"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        heada = headA
        headb = headB

        ha = []
        while heada:
            ha.append(heada)
            heada = heada.next

        hb = []
        while headb:
            hb.append(headb)
            headb = headb.next

        i = len(ha) - 1
        j = len(hb) - 1

        while i >= 0 and j >= 0:

            if ha[i] != hb[j]:
                return None if (i + 1 >= len(ha) or j + 1 >= len(hb)) else ha[i + 1]

            i = i - 1
            j = j - 1

        return ha[i + 1]


if __name__ == '__main__':
    # [4,1,8,4,5]
    # [5,6,1,8,4,5]
    nodes = ListNode(8, ListNode(4, ListNode(5, )))
    nodeA = ListNode(4, ListNode(1, nodes))
    nodeB = ListNode(5, ListNode(6, ListNode(1, nodes)))

    c = Solution()
    rez = c.getIntersectionNode(nodeA, nodeB)
    print(rez.val)

