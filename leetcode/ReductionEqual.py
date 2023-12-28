class Reduc:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                res += len(nums) - i
        return res


if __name__ == '__main__':
    red = Reduc()
    digits = [1, 1, 2, 2, 3]
    print(red.reductionOperations(digits))