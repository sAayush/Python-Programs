class BinAdd:
    def addBinary(self, a: str, b: str) -> str:
        # print(a, b)
        # print(int(a, 2), int(b, 2))
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a = '11'
    b = '1'
    bin_add = BinAdd()
    print(bin_add.addBinary(a, b))
