class Bits:
    def hammingWeight(self, n: int) -> int:
        res = []
        ns = str(n)
        for i in range(len(ns)):
            res.append(ns[i])
        return res.count('1')


if __name__ == '__main__':
    bits = Bits()
    b = 10000000000000000000000000000011
    print(bits.hammingWeight(b))
