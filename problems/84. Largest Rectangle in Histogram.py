class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        left = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) > 0:
                left.append(stack[-1])
            else:
                left.append(-1)

            stack.append(i)

        stack = []
        right = [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) > 0:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)

            stack.append(i)

        s = 0
        for i, item in enumerate(heights):
            sq = item * (right[i] - left[i] - 1)
            if sq > s:
                s = sq
        return s