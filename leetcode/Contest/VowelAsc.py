class Vowel:
    def sortVowels(self, s: str) -> str:

        if 'aeiouAEIOU'.find(s) != -1:
            return s
        vow = []
        for i in range(len(s)):
            if 'aeiouAEIOU'.find(s[i]) != -1:
                vow.append(s[i])
        j = 0
        vow.sort()

        for i in range(len(s)):
            if 'aeiouAEIOU'.find(s[i]) != -1:
                s = s[:i] + vow[j] + s[i + 1:]
                j += 1
        return s

        # vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        # count_char = Counter(s)
        # s_vowels = []
        # for char in count_char.keys():
        #     if char in vowels:
        #         s_vowels.append(char)
        #         s = s.replace(char, '_')
        # s_vowels.sort()
        # for char in s_vowels:
        #     s = s.replace('_', char, count_char[char])
        # return s


if __name__ == '__main__':
    vowel = Vowel()
    s = "lEetcOde"
    print(vowel.sortVowels(s))
