"""
https://leetcode.com/problems/sort-colors/

https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        store = [0] * 3
        for item in nums:
            store[item] += 1

        nums[0:store[0]] = [0] * store[0]
        nums[store[0]:store[0] + store[1]] = [1] * store[1]
        nums[store[0] + store[1]:] = [2] * store[2]

    # The unknown section is shrunk while maintaining these conditions:
    # Lo := 1; Hi := N;
    # while Lo <= Hi do
    # Invariant: a[1..Lo-1] are all zero and a[Hi+1..N] are all one; a[Lo..Hi] are unknown.
    # if a[Lo] = 0 then Lo++
    # else swap a[Lo] and a[Hi]; Hi--

    def twoColor(self, nums):
        low = 0
        hi = len(nums) - 1

        while low < hi:
            if nums[low] == 0:
                low += 1
            else:
                nums[low], nums[hi] = nums[hi], nums[low]
                hi -= 1

    # The unknown region is shrunk while maintaining these conditions
    # Lo := 1; Mid := 1; Hi := N;
    # while Mid <= Hi do
    # Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and a[Hi+1..N]=2; a[Mid..Hi] are unknown.
    # case a[Mid] in
    # 0: swap a[Lo] and a[Mid]; Lo++; Mid++
    # 1: Mid++
    # 2: swap a[Mid] and a[Hi]; Hi--

    def threeColor(self, nums):
        low, middle, hi = 0, 0, len(nums) - 1

        while middle <= hi:
            if nums[middle] == 0:
                nums[low], nums[middle] = nums[middle], nums[low]
                low += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[hi], nums[middle] = nums[middle], nums[hi]
                hi -= 1


if __name__ == '__main__':
    s = Solution()
    # data = [2, 0, 2, 1, 1, 1]
    data = [1, 0, 0, 1, 1, 0]
    # s.sortColorsInplace(data)
    s.threeColor(data)
    print(data)
