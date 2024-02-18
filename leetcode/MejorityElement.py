class MejElement:
    def majorityElement(self, nums: list[int]) -> int:
        # # 2 pointer method
        # count = 0
        # candidate = None
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)
        # return candidate

        # # Hashmap method
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        # for k, v in d.items():
        #     if v > len(nums) / 2:
        #         return k

        # # Sorting method
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    me = MejElement()
    print(me.majorityElement([3, 2, 3]))  # 3
