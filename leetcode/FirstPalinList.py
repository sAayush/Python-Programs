class FirstPalin:
    def firstPalindrome(self, words: list[str]) -> str:
        # # Brute force
        #
        # for word in words:
        #     if word == word[::-1]:
        #         return word
        # return ""

        # Optimized
        for i in range(len(words)):
            left = 0
            right = len(words[i]) - 1
            while left < right:
                if words[i][left] != words[i][right]:
                    break
                left += 1
                right -= 1
            if left >= right:
                return words[i]
        return ""


if __name__ == "__main__":
    firstPalin = FirstPalin()
    print(firstPalin.firstPalindrome(["racecar", "apple", "aba"])) # racecar
