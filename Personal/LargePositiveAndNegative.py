class PosNegative:
    def findMaxK(self, nums: list[int]) -> int:
        # two pointer
        # nums.sort()
        # # if nums[0] > 0:
        # #     return -1
        # # if nums[-1] < 0:
        # #     return -1
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if nums[i] + nums[j] == 0:
        #         return nums[j]
        #     elif abs(nums[i]) > nums[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return -1

        # Brute force
        # m = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == 0:
        #             m = max(m, abs(nums[j]))
        # if m == 0:
        #     return -1
        # return m

        # Hashmap
        d = {}
        m = 0
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            if -nums[i] in d:
                m = max(m, abs(nums[i]))
        if m == 0:
            return -1
        return m


if __name__ == '__main__':
    pn = PosNegative()
    print(pn.findMaxK([-1, 2, -3, 3]))
    print(pn.findMaxK([1, 2, -1, 3, -3, 10, 4, -10]))

