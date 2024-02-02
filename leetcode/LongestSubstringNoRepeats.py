class subs:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = []
        max = 0
        tempmax = 0
        for i in range(len(s)):
            if s[i] not in store:
                store.append(s[i])
                if len(store) > max:
                    max = len(store)
            else:
                while s[i] in store:
                    store.pop(0)
                store.append(s[i])
                if max > tempmax:
                    tempmax = max
                max = 1

        if tempmax > max:
            return tempmax
        else:
            return max


if __name__ == '__main__':
    s = subs()
    print(s.lengthOfLongestSubstring("abcabcbb"))