class DivSubset:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        # Using DP

        nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                print("this is I", i)
                print("this is J", j)
                print(range(i))
                print(nums[i] % nums[j] == 0)
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(dp)
        max_val = max(dp)
        max_index = dp.index(max_val)
        res = [nums[max_index]]
        for i in range(max_index - 1, -1, -1):
            print("max val", max_val)
            print("this is I", i)
            print("this is res", res)
            if res[-1] % nums[i] == 0 and dp[i] == max_val - 1:
                res.append(nums[i])
                print(res)
                max_val -= 1
        return res[::-1]


if __name__ == "__main__":
    ds = DivSubset()
    print(ds.largestDivisibleSubset([1, 2, 3]))  # [1, 2]
    print("###############################")
    print(ds.largestDivisibleSubset([1, 2, 4, 8]))  # [1, 2, 4, 8]
    # print(ds.largestDivisibleSubset([4, 8, 10, 240]))  # [4, 8, 240]
