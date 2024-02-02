class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(word1)):
            count1[ord(word1[i]) - ord('a')] += 1
            count2[ord(word2[i]) - ord('a')] += 1

        # print(count1)
        # print(count2)

        for i in range(26):
            if (count1[i] == 0 and count2[i] != 0) or (count1[i] != 0 and count2[i] == 0):
                return False

        return sorted(count1) == sorted(count2)