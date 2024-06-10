class AppendSubsequence:
    def appendCharacters(self, s: str, t: str) -> int:
        ti = 0
        l = len(s)
        for i in range(l):
            if s[i] == t[ti]:
                ti += 1
                if len(t) == ti:
                    return 0
        
        return len(t) - ti
    

if __name__ == '__main__':
    asb = AppendSubsequence()
    s = 'coaching'
    t = 'coding'
    print(asb.appendCharacters(s, t))
    
