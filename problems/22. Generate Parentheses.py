"""
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.recGenerateParenthesis('', n, n)

        return self.result

    def recGenerateParenthesis(self, data, close, open):

        if close + open == 0:
            self.result.append(data)
            return

        if close <= open:
            self.recGenerateParenthesis(data + '(', close=close, open=open - 1)
        elif open == 0:
            self.recGenerateParenthesis(data + ')', close=close - 1, open=open)
        else:
            self.recGenerateParenthesis(data + '(', close=close, open=open - 1)
            self.recGenerateParenthesis(data + ')', close=close - 1, open=open)

    def generateParenthesis2(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,

            return parens

        return generate('', n, n)

    def recGenerateParenthesis3(self, data, close, open):

        if open > 0:
            self.recGenerateParenthesis(data + '(', close=close, open=open - 1)
        if close > open:
            self.recGenerateParenthesis(data + ')', close=close - 1, open=open)

        if close == 0:
            self.result.append(data)


if __name__ == '__main__':
    s = Solution()
    data = ''
    s.result = []
    s.recGenerateParenthesis3('', 3, 3)
    print(s.result)


