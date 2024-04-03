class Climbing:
    def climbStairs(self, n):
        # if n == 1:
        #     return 1
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second


if __name__ == '__main__':
    c = Climbing()
    print(c.climbStairs(2)) # 2
    print(c.climbStairs(3)) # 3
    print(c.climbStairs(4)) # 5