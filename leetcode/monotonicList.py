class Monotonic:
    def isMonotonic(nums: list[int]) -> bool:
        inc = False
        dec = False

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc = True
                if dec:
                    return False
            elif nums[i] > nums[i + 1]:
                dec = True
                if inc:
                    return False
        return True


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    # nums = [6, 5, 4, 4]
    print(Monotonic.isMonotonic(nums))

