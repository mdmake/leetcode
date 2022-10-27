# Definition for singly-linked list.
"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
https://www.youtube.com/watch?v=8rccK-8gJDo
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

        while heada != headb:
            heada = heada.next if (heada is not None) else headB
            headb = headb.next if (headb is not None) else headA

        return heada


if __name__ == '__main__':
    # [4,1,8,4,5]
    # [5,6,1,8,4,5]
    nodes = ListNode(8, ListNode(4, ListNode(5, )))
    nodeA = ListNode(4, ListNode(1, nodes))
    nodeB = ListNode(5, ListNode(6, ListNode(1, nodes)))

    c = Solution()
    rez = c.getIntersectionNode(nodeA, nodeB)
    print(rez.val)
