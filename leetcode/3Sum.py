class Sum3Zero:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Brute force
        # nums.sort()
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.append([nums[i], nums[j], nums[k]])
        # res = list(set(tuple(sublist) for sublist in res))
        # res = [list(t) for t in res]
        # return res

        # two pointers

        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    nums = [3, 0, -2, -1, 1, 2]
    s3z = Sum3Zero()
    print(s3z.threeSum(nums))


