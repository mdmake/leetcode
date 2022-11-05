"""
https://leetcode.com/problems/sort-an-array/

https://practicum.yandex.ru/learn/algorithms/courses/7f101a83-9539-4599-b6e8-8645c3f31fad/sprints/16095/topics/4a0eb007-5d71-4dda-bc54-df8c743f80ea/lessons/dd0cc4cc-6738-4aea-ab35-ce21674dc2c6/
"""

from typing import List


def mergeSort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    part1 = mergeSort(data[:mid])
    part2 = mergeSort(data[mid:])

    i, j = 0, 0
    rezult = []

    while i < len(part1) and j < len(part2):
        if part1[i] < part2[j]:
            rezult.append(part1[i])
            i += 1
        else:
            rezult.append(part2[j])
            j += 1

    while j < len(part2):
        rezult.append(part2[j])
        j += 1
    while i < len(part1):
        rezult.append(part1[i])
        i += 1

    return rezult


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return mergeSort(nums)


if __name__ == '__main__':
    s = Solution()
    data = [5, 2, 3, 1]
    rez = s.sortArray(data)
    print(rez)
