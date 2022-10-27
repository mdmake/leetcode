"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""

from collections import deque


class Solution:
    def maxDepth(self, s: str) -> int:

        stack = deque()

        max_depth = 0
        for item in s:
            if item == '(':
                stack.append('(')
                max_depth = max(max_depth, len(stack))
            elif item == ')':
                stack.pop()
        return max_depth
