"""
https://leetcode.com/problems/binary-search/submissions/
"""

from typing import List


class Solution:

    def binarySearch(self, data, left, right, target):

        if target < data[left] or target > data[right]:
            return -1

        mid = left + (right - left) // 2

        if data[mid] == target:
            return mid

        if target > data[mid]:
            return self.binarySearch(data, mid + 1, right, target)
        else:
            return self.binarySearch(data, left, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:

        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def search_twopointers(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    data = [-1,0,3,5,9,12]

    print(s.search_twopointers(data, -10))
    print(s.search_twopointers(data, -15))
    print(s.search_twopointers(data, 10))

    for item in data:
        print(s.search_twopointers(data, item))
