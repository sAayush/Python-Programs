class AfterDeleting:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                break
            while l < r and s[l] == s[l+1]:
                l += 1
                if l == r:
                    return 0
            while l < r and s[r] == s[r-1]:
                if l == r:
                    return 0
                r -= 1
            l += 1
            r -= 1

        print(l, r)
        return r - l + 1


if __name__ == '__main__':
    ad = AfterDeleting()
    print(ad.minimumLength("cabaabac"))
