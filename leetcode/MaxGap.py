class MaxGap:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        mg = 0
        
        for i in range(1, len(nums)):
            mg = max(mg, nums[i] - nums[i-1])
            
        return mg
    

if __name__ == '__main__':
    mag = MaxGap()
    print(mag.maximumGap([3,6,9,1])) # 3
        