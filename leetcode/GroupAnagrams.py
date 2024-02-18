class Anagram:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using dictionary

        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        return list(d.values())


if __name__ == '__main__':
    a = Anagram()
    print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]
