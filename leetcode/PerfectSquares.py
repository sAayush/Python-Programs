class PerfectSquareSum:
    def numSquares(self, n: int) -> int:
        # Using BFS
        q = [n]
        level = 0
        while q:
            level += 1
            new_q = []
            for i in q:
                j = 1
                while j * j <= i:
                    # print("this is I", i)
                    # print("this is J", j * j)
                    if i - j * j == 0:
                        # print(new_q)
                        # print(level)
                        # print("this is J", j)
                        return level
                    new_q.append(i - j * j)
                    # print(new_q)
                    j += 1
            q = new_q
        return level

        # # Using DP
        #
        # dp = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     j = 1
        #     min_val = float('inf')
        #     while j * j <= i:
        #         min_val = min(min_val, dp[i - j * j])
        #         j += 1
        #     dp[i] = min_val + 1
        # return dp[n]


if __name__ == "__main__":
    ps = PerfectSquareSum()
    print(ps.numSquares(12))  # 3
