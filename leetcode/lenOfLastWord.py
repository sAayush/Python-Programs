class LenLast:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])


if __name__ == '__main__':
    ll = LenLast()
    print(ll.lengthOfLastWord('Hello World')) # 5