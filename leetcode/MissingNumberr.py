class MissNum:
    def missingNumber(self, nums: list[int]) -> int:
        # n = len(nums)
        # return n * (n + 1) // 2 - sum(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)


if __name__ == "__main__":
    ms = MissNum()
    print(ms.missingNumber([3, 0, 1, 4, 5]))  # 2