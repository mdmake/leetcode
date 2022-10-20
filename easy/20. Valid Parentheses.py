from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        data = {'}': '{', ')': '(', ']': '['}

        stack = deque()

        for bracket in s:
            try:
                if bracket not in data.keys():
                    stack.append(bracket)
                elif stack.pop() != data[bracket]:
                    return False
            except:
                return False

        if len(stack) > 0:
            return False

        return True
