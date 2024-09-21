class UncommonWords:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split() + s2.split()
        res = []
        for word in words:
            if words.count(word) == 1:
                res.append(word)
        return res
        

if __name__ == '__main__':
    uw = UncommonWords()
    print(uw.uncommonFromSentences("this apple is sweet", "this apple is sour")) # ["sweet","sour"]