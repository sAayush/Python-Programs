class JumpGameII:
    def jump(self, nums: list[int]) -> int:
        # Solved using Greedy approach
        # where we keep track of the current farthest index we can reach
        # and the current end of the jump
        # if we reach the end of the jump we increment the jumps
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] == 0:
            return 0
        jumps = 0
        cur_end = 0
        cur_farthest = 0
        for i in range(n-1):
            cur_farthest = max(cur_farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        return jumps


if __name__ == '__main__':
    nums = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9, 1, 1, 1, 1, 1]
    s = JumpGameII()
    print(s.jump(nums))
