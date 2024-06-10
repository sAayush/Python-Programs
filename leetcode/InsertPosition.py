class PosIn:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


if __name__ == '__main__':
    pi = PosIn()
    print(pi.searchInsert([1, 3, 5, 6], 5))