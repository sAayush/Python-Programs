class LongestSubarrayAnd:
    def longestSubarray(self, nums: list[int]) -> int:
        target = max(nums)
        count, maxcount = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
                
        return maxcount
    

if __name__ == '__main__':
    lsa = LongestSubarrayAnd()
    print(lsa.longestSubarray([1, 2, 3, 3, 2, 2])) # 2