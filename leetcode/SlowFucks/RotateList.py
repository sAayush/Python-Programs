class Rotate:
    def maxRotateFunction(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        res = []
        for i in range(len(nums)):
            res.append(self.rotate(nums, i))
        return max(res)

    def rotate(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            res += i * nums[i - k]
        return res


if __name__ == '__main__':
    rotate = Rotate()
    nums = [1, 2, 3, 4]
    print(rotate.maxRotateFunction(nums))
