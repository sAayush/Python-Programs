class Samelist:
    def numIdenticalPairs(nums: list[int]) -> int:
        # how this method works:
        # 1. for each element in the list, count the number of elements that are the same as it
        # 2. add the number of elements that are the same as it to the total number of pairs
        # 3. return the total number of pairs
        return sum([sum([1 for j in range(i + 1, len(nums)) if nums[i] == nums[j]]) for i in range(len(nums))])


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    print(Samelist.numIdenticalPairs(nums))
