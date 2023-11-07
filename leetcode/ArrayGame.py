class ArrGame:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)

        winner = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]
                wins = 1
            if wins == k:
                return winner
        return winner


if __name__ == '__main__':
    ag = ArrGame()
    lis = [2, 1, 3, 5, 4, 6, 7]
    k = 2
    print(ag.getWinner(lis, k))

