class SetMismatch:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dup = -1
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]


if __name__ == '__main__':
    sm = SetMismatch()
    print(sm.findErrorNums([1, 2, 2, 4]))  # [2, 3]
