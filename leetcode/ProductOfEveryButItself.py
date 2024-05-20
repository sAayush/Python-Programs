class ProductList:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Too slow didnt work
        # lenn = len(nums)
        # ans = [1] * lenn
        # for i in range(lenn):
        #     for j in range(lenn):
        #         if i != j:
        #             ans[i] *= nums[j]
        # return ans
        lenn = len(nums)
        ans = [1] * lenn
        left = 1
        right = 1
        for i in range(lenn):
            ans[i] *= left
            left *= nums[i]
            ans[lenn-i-1] *= right
            right *= nums[lenn-i-1]
        return ans


if __name__ == '__main__':
    pl = ProductList()
    print(pl.productExceptSelf([1, 2, 3, 4]))
