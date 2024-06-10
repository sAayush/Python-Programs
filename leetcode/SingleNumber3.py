class SingleNumber:
    def singleNumber(self, nums: list[int]) -> list[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    single_number = SingleNumber()
    print(single_number.singleNumber(nums))