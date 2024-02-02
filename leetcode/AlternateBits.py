class Bits:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1":
                count += 1
            elif i % 2 == 1 and s[i] == "0":
                count += 1
        return min(count, len(s) - count)


if __name__ == "__main__":
    B = Bits()
    s = "0100"
    print(B.minOperations(s))
