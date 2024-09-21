class ShortestPalin:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        print('After I: ',s[i:])
        print('After I and ::-1: ',s[i:][::-1])
        print('function output: ',self.shortestPalindrome(s[:i]))
        print('adding s[i+]: ',s[i:])
        return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]
    

if __name__ == '__main__':
    sp = ShortestPalin()
    print(sp.shortestPalindrome('aacecaaa')) # aaacecaaa