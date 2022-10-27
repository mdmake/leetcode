"""
https://leetcode.com/problems/remove-outermost-parentheses/submissions/
"""

from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        news = ''
        stack = deque()

        for item in s:
            if item == '(':
                stack.append('(')
            elif item == ')':
                stack.pop()

            if len(stack) != 1:
                news += item

        return news

    def removeOuterParentheses_1(self, s: str) -> str:

        news = ''
        stack = 0

        for item in s:
            if item == '(':
                stack += 1

            if stack != 1:
                news += item

            if item == ')':
                stack -= 1

        return news

    def removeOuterParentheses_fast(self, s: str) -> str:

        res = []
        stack = 0

        for item in s:
            if item == '(':
                stack += 1

            if stack != 1:
                res.append(item)

            if item == ')':
                stack -= 1

        return ''.join(res)


if __name__ == '__main__':
    pass
