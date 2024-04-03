class LongPalin:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        ans = 0
        odd = False
        for c in count.values():
            if c % 2 == 0:
                ans += c
            else:
                ans += c - 1
                odd = True
        return ans + 1 if odd else ans


if __name__ =='__main__':
    lp = LongPalin()
    print(lp.longestPalindrome('abccccdd')) # 7
