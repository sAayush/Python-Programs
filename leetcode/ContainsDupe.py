class ContainsDupe:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # we can use a set to store the numbers
        # and check if the number is already in the set
        # if it is we return True
        # otherwise we add the number to the set
        # and return False
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
    

if __name__ == "__main__":
    cd = ContainsDupe()
    print(cd.containsDuplicate([1,2,3,1])) # True