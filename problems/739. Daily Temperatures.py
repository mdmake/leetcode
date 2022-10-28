from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rez = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if len(stack) > 0:
                rez[i] = stack[-1][0] - i

            stack.append((i, temperatures[i]))

        return rez
