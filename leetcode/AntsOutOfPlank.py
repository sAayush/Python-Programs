class Ants:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        res = 0
        for i in left:
            res = max(res, i)
        for i in right:
            res = max(res, n - i)
        return res


if __name__ == '__main__':
    ants = Ants()
    n = 4
    left = [4, 3]
    right = [0, 1]
    print(ants.getLastMoment(n, left, right))