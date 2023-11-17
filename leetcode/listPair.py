class ListPair:
    def minPairSum(self, nums: list[int]) -> int:
        # nums.sort()
        # res = 0
        # for i in range(len(nums) // 2):
        #     res = max(res, nums[i] + nums[len(nums) - i - 1])
        # return res

        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0

        while left < right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    lp = ListPair()
    lis = [3, 5, 2, 3]
    print(lp.minPairSum(lis))