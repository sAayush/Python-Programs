class ListString:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


if __name__ == '__main__':
    listString = ListString()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(listString.arrayStringsAreEqual(word1, word2))