class Judge:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        trust_count = [0] * (n+1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        for i in range(1, n+1):
            if trust_count[i] == n-1:
                return i
        return -1


if __name__ == '__main__':
    j = Judge()
    print(j.findJudge(2, [[1,2]])) # 2
