class Coins:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        res = 0
        for i in range(len(piles) - 2, (len(piles) // 3) - 1, -2):
            res += piles[i]
        return res


if __name__ == '__main__':
    coins = Coins()
    piles = [2, 4, 1, 2, 7, 8]
    print(coins.maxCoins(piles))