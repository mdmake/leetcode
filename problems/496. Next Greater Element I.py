from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        #nge = [-1] * len(nums2)
        nge = dict()

        for i, item in enumerate(nums2):
            while len(stack) > 0 and nums2[stack[-1][0]] < item:
                idx, val = stack.pop()
                nge[val] = item

            stack.append((i, item))

        nge2 = [0] * len(nums1)
        for i, item in enumerate(nums1):
            nge2[i] = nge.get(item,-1)

        return nge2


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
