class Diff:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                res.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return res


if __name__ == '__main__':
    d = Diff()
    print(d.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 3))
