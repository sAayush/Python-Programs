# class Solution:
#     def sortArrayByParity(nums: list[int]) -> list[int]:
#         i, j = 0, len(nums) - 1
#
#         while i < j:
#             while i < j and nums[i] % 2 == 0:
#                 i += 1
#             while i < j and nums[j] % 2 == 1:
#                 j -= 1
#
#             nums[i], nums[j] = nums[j], nums[i]
#
#         return nums

class SortPair:
    @staticmethod
    def sortArrayByParity(nums: list[int]) -> list[int]:
        i = 0
        ins = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                nums[ins], nums[i] = nums[i], nums[ins]
                ins += 1
            i += 1
        return nums


if __name__ == '__main__':
    sp = SortPair
    mixNums = [3, 1, 2, 4]
    print(sp.sortArrayByParity(mixNums))
