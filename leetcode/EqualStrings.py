class EqualString:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
        count = 0
        for i in range(len(s) // 2):
            if s[i] in vowels:
                count += 1
            if s[len(s) - 1 - i] in vowels:
                count -= 1
        return count == 0


if __name__ == "__main__":
    ES = EqualString()
    s = "book"
    print(ES.halvesAreAlike(s))