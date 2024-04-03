class MinCommonList:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        # Too slow didnt work
        # return min([x for x in nums1 if x in nums2])
        nums1 = set(nums1)
        nums2 = set(nums2)
        num = nums1 & nums2
        if num:
            return min(num)
        return -1


if __name__ == '__main__':
    mcl = MinCommonList()
    print(mcl.getCommon([1, 2, 3, 4], [2, 3, 4, 5])) # 2
