class Solution:
    def longestPalindrome(self, words) -> int:

        data = dict()

        for item in words:
            data[item] = data.get(item, 0) + 1

        lngth = 0
        used = set()
        for k in data.keys():

            if k not in used:
                rk = k[1] + k[0]

                if rk == k:
                    if data[k] > 1:
                        lngth += (data[k] // 2) * 4
                        data[k] = data[k] % 2
                        #used.add(k)


                elif rk in data.keys() and rk not in used and k not in used:
                    lngth += min(data[rk] * 4, data[k] * 4)
                    used.add(rk)
                    used.add(k)

        mddl = 0

        for k, v in data.items():
            if v == 1 and k[0] == k[1] and k not in used:
                mddl = 2
                break

        return mddl + lngth


if __name__ == '__main__':
    s = Solution()
    data = ["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]
    print(s.longestPalindrome(data))
