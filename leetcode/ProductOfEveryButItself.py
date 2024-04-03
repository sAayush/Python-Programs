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
        left = [1] * lenn
        right = [1] * lenn
        ans = [1] * lenn



if __name__ == '__main__':
    pl = ProductList()
    print(pl.productExceptSelf([1, 2, 3, 4]))
