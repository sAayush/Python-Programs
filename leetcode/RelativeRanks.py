class RelativeRanks:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        d = {}
        for i, s in enumerate(score):
            d[s] = i



if __name__ == '__main__':
    score = [5, 4, 3, 2, 1]
    rr = RelativeRanks()
    print(rr.findRelativeRanks(score))
