class CheapFlights:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = 1e9
        dp = [INF] * n
        dp[src] = 0
        for i in range(k+1):
            temp = dp[:]
            for u, v, w in flights:
                temp[v] = min(temp[v], dp[u] + w)
            dp = temp
        return dp[dst] if dp[dst] < INF else -1


if __name__ == '__main__':
    cf = CheapFlights()
    print(cf.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)) # 200
    print(cf.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)) # 500
