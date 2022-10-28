"""
42. Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = [0, ]
        maxRight = [0, ]

        for num in height[:-1]:
            maxLeft.append(max(num, maxLeft[-1]))

        # print(maxLeft)

        for num in height[:0:-1]:
            maxRight.append(max(num, maxRight[-1]))

        maxRight = maxRight[::-1]
        # print(maxRight)

        minLR = [min(l, r) for l, r in zip(maxLeft, maxRight)]
        # print(minLR)

        volume = 0

        for d, h in zip(minLR, height):
            volume += max(d - h, 0)

        return volume
