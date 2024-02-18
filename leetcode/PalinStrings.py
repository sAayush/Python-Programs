class PalStrs:
    def countSubstrings(self, s: str) -> int:
        # # Using Brute Force
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        return count


if __name__ == "__main__":
    ps = PalStrs()
    print(ps.countSubstrings("abc"))  # 3
    print(ps.countSubstrings("aaa"))  # 6