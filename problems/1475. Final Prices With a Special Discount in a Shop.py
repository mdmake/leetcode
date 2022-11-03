from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        discount = [0] * len(prices)

        stack = []

        for i in range(len(prices) - 1, -1, -1):

            while len(stack) > 0 and stack[-1] > prices[i]:
                stack.pop()

            if len(stack) > 0:
                discount[i] = prices[i] - stack[-1]
            else:
                discount[i] = prices[i]

            stack.append(prices[i])

        return discount