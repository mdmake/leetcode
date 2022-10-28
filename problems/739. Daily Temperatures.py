"""
https://leetcode.com/problems/daily-temperatures/

https://www.youtube.com/watch?v=cTBiBSnjO3c&t=3s
https://www.youtube.com/watch?v=cTBiBSnjO3c&t=3s
https://www.youtube.com/watch?v=WGm4Kj3lhRI
"""

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

    # обратный
    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        rez = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):

            while len(stack) > 0 and stack[-1][1] <= temperatures[i]:
                stack.pop()

            if len(stack) > 0:
                rez[i] = stack[-1][0] - i

            stack.append((i, temperatures[i]))

        return rez

    def dailyTemperatures_3(self, temperatures: List[int]) -> List[int]:
        rez = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1][0]] < t:
                cur = stack.pop()[0]
                rez[cur] = i - cur
            stack.append((i, t))

        return rez


if __name__ == '__main__':
    s = Solution()

    print(s.dailyTemperatures_3([73, 74, 75, 71, 69, 72, 76, 73]))
