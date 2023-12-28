class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    digits = [1, 1, 2, 2, 3]
    print(solution.removeDuplicates(digits))