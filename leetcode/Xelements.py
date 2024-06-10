class XElementsGreater:
    def specialArray(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1
            if count == i:
                return i
        return -1


if __name__ == '__main__':
    nums = [3, 5]
    x_elements = XElementsGreater()
    print(x_elements.specialArray(nums))
