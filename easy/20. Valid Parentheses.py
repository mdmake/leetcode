from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        data = {'}': '{', ')': '(', ']': '['}

        stack = deque()

        for bracket in s:
            if bracket not in data.keys():
                stack.append(bracket)
            elif len(stack) == 0 or stack.pop() != data[bracket]:
                return False

        return len(stack) == 0
