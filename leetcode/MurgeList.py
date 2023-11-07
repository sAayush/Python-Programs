class MurgeList:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
        print(nums1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    MurgeList.merge(nums1, m, nums2, n)