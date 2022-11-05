class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        dc = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def genCombination(data, digit, result=[]):

            if len(digit) == 0:
                result += data,
            else:
                for item in dc[digit[0]]:
                    genCombination(data + item, digit[1:])

            return result

        return genCombination("", digits)

