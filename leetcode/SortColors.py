class SortCol:
    def sortColors(self, nums: list[int]):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    
if __name__ == '__main__':
    sc = SortCol()
    print(sc.sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]
    
    