class longVowel:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            an = (e) % MOD
            en = (a + i) % MOD
            in_ = (a + e + o + u) % MOD
            on = (i + u) % MOD
            un = (a) % MOD

            a, e, i, o, u = an, en, in_, on, un

        return (a + e + i + o + u) % MOD


if __name__ == '__main__':
    obj = longVowel()
    print(obj.countVowelPermutation(5))

