from typing import List


class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        nums.sort()  # Use nums.sort() instead of List.sort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


# Create an instance of the Solution class
solution = Solution()

# Call the findDuplicate method on the instance
my_list = [1, 3, 4, 2, 2]
result = solution.findDuplicate(my_list)

print(result)
