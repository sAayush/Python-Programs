class StringContainsCount:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    break
            else:
                count += 1
        return count


if __name__ == '__main__':
    scc = StringContainsCount()
    print(scc.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))