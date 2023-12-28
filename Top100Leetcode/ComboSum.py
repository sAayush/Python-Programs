class ComSum:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(tar, lis, idx):
            if tar == target:
                res.append(lis.copy())
                return

            if tar > target:
                return

            for i in range(idx, len(candidates)):
                lis.append(candidates[i])
                dfs(tar + candidates[i], lis, i)
                lis.pop()

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    comSum = ComSum()
    cand = [2, 3, 6, 7]
    targ = 7
    print(comSum.combinationSum(cand, targ))
