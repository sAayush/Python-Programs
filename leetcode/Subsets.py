class Subset:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result
        # result = []
        # def backtrack(start, path):
        #     result.append(path)
        #     for i in range(start, len(nums)):
        #         backtrack(i+1, path + [nums[i]])
        # backtrack(0, [])
        # return result


if __name__ == '__main__':
    s = Subset()
    print(s.subsets([1, 2, 3]))