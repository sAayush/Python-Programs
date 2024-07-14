class SingleNum:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
    
if __name__ == "__main__":
    sn = SingleNum()
    print(sn.singleNumber([2,2,1])) # 1