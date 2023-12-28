class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[len(digits) - 1] < 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            digits[len(digits) - 1] = 0
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
            digits.insert(0, 1)
            return digits


if __name__ == '__main__':
    solution = Solution()
    digits = [9, 9, 9]
    print(solution.plusOne(digits))
