class Subset:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, lis, res):
        # It works by appending the current list to the result list
        # and then iterating through the rest of the list and appending
        # the current element to the list and then calling the function
        # again with the rest of the list and the current list. Then
        # popping the current element from the list and repeating the
        # process until the list is empty.
        res.append(lis.copy())
        for i in range(len(nums)):
            lis.append(nums[i])
            self.dfs(nums[i + 1:], lis, res)
            lis.pop()


if __name__ == '__main__':
    subset = Subset()
    nums = [1, 2, 3]
    print(subset.subsets(nums))