class Frequent:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        res = 1
        total = 0
        while right < len(nums):
            total += nums[right]
            while total + k < nums[right] * (right - left + 1):
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    freq = Frequent()
    lis = [1, 2, 4]
    k = 5
    print(freq.maxFrequency(lis, k))