class Solution:

    def decomposeNumber(self, num: int) -> list:
        if num < 4:
            return [1, ] * num
        if num == 4:
            return [4, ]
        if num < 9:
            return [5, ] + [1, ] * (num - 5)
        if num == 9:
            return [9, ]

    def intToRoman(self, num: int) -> str:
        data = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            900: 'CM',
            500: 'D',
            1000: 'M',
        }

        digits = str(num)
        digits = '0' * (4 - len(digits)) + digits

        result = []
        for digit, r in zip(digits, [1000, 100, 10, 1]):
            result += [item * r for item in self.decomposeNumber(int(digit))]

        roman = ''
        for item in result:
            roman = roman + data[item]

        return roman

if __name__ == '__main__':

    s = Solution()

    print(s.intToRoman(1))
    print(s.intToRoman(10))
    print(s.intToRoman(100))
    print(s.intToRoman(1000))
    print(s.intToRoman(1994))
