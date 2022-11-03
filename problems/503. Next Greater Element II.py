"""

https://leetcode.com/problems/next-greater-element-ii/submissions/
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        i = 0
        nge = [-1] * len(nums)
        stack = []

        count = 0

        while count < len(nums) * 2:

            # for i in range(0, len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                nge[idx] = nums[i]

            count += 1
            stack.append(i)

            i = (i + 1) % len(nums)

        return nge

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:

        nge = [-1] * len(nums)
        stack = []

        for i in range(0, len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                nge[stack.pop()] = nums[i]

            stack.append(i)

        for i in range(0, len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                nge[stack.pop()] = nums[i]

        return nge


if __name__ == '__main__':
    s = Solution()
    data = [1, 2, 3, 4, 3]
    print(s.nextGreaterElements2(data))
