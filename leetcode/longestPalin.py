class Palindrome:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # print(d)
        res = 0
        odd = False
        for i in d:
            if d[i] % 2 == 0:
                res += d[i]
            if d[i] % 2 == 1:
                res += d[i] - 1
                odd = True
        if odd:
            res += 1
        return res


if __name__ == '__main__':
    p = Palindrome()
    print(p.longestPalindrome("abccccdd"))
