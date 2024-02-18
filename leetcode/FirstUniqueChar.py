# import collections as c

class UniqChar:
    def firstUniqChar(self, s: str) -> int:

        # # Brute force

        # flag = False
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if i != j and s[i] == s[j]:
        #             flag = False
        #             break
        #         else:
        #             flag = True
        #
        #     if flag:
        #         return i
        # return -1

        # # Using Counter

        # sc = c.Counter(s)
        # for i in range(len(s)):
        #     if sc[s[i]] == 1:
        #         return i
        # return -1

        # Using dictionary

        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    uc = UniqChar()
    print(uc.firstUniqChar("leetcode"))  # 0
