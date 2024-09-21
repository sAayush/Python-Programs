class LargestNumber:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))\
        # works becasue of the nature of string comparison in python
        # x * 10 = 3 * 10 = 3333333333
        # x * 10 = 30 * 10 = 30303030303030303030
        # but 3 == 3 and 3 > 0 so 3 > 30
        # so 3 will come before 30
        # Works the same in other as well
        nums.sort(key=lambda x: x*10, reverse=True)
        return str(int(''.join(nums)))
    

if __name__ == '__main__':
    ln = LargestNumber()
    lis = [3, 30, 34, 5, 9]
    print(ln.largestNumber(lis))