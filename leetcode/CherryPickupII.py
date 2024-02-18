class CherryPickupHard:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}
        def dp(r, c1, c2):
            if r == rows or c1 < 0 or c1 == cols or c2 < 0 or c2 == cols:
                return 0
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            maxCherries = 0

            for dp1 in [-1, 0, 1]:
                for dp2 in [-1, 0, 1]:
                    maxCherries = max(maxCherries, dp(r + 1, c1 + dp1, c2 + dp2))
            memo[(r, c1, c2)] = cherries + maxCherries
            return memo[(r, c1, c2)]
        return dp(0, 0, cols - 1)


if __name__ == '__main__':
    cph = CherryPickupHard()
    grd = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(cph.cherryPickup(grd))  # 24
