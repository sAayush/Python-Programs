class LargestParameter:
    def largestPerimeter(self, nums: list[int]) -> int:
        # prefix sum
        nums.sort()
        tsum = sum(nums)
        for i in range(len(nums) - 1, 1, -1):
            if tsum - nums[i] > nums[i]:
                return tsum
            else:
                tsum -= nums[i]
        return -1


if __name__ == "__main__":
    lp = LargestParameter()
    print(lp.largestPerimeter([5, 5, 5]))  # 15
    print(lp.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))  # 12
