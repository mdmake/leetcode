"""
https://leetcode.com/problems/sort-an-array/

https://practicum.yandex.ru/learn/algorithms/courses/7f101a83-9539-4599-b6e8-8645c3f31fad/sprints/16095/topics/4a0eb007-5d71-4dda-bc54-df8c743f80ea/lessons/dd0cc4cc-6738-4aea-ab35-ce21674dc2c6/
"""
from typing import List


def quickSort1(nums):
    def helper(head, tail):
        if head >= tail: return
        l, r = head, tail
        m = (r - l) // 2 + l
        pivot = nums[m]
        while r >= l:
            while r >= l and nums[l] < pivot: l += 1
            while r >= l and nums[r] > pivot: r -= 1
            if r >= l:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        helper(head, r)
        helper(l, tail)

    helper(0, len(nums) - 1)
    return nums


def partition(array, pivot, i, j):
    while i <= j:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return i, j


def quickSort(data, i, j):
    if i >= j:
        return

    mid = i + (j - i) // 2
    pivot = data[mid]

    l, r = partition(data, pivot, i, j)

    quickSort(data, i, r)
    quickSort(data, l, j)

    return


def mergeSort(data):
    if len(data) > 1:

        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mergeSort(nums)


if __name__ == '__main__':
    s = Solution()
    data = [5, 1, 1, 2, 0, 0]
    # data = [-2, 3, -5]
    # data = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
    # mergeSort(data)
    # data = quickSort1(data)
    quickSort(data, 0, len(data) - 1)
    print(data)
