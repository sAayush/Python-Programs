class Binary:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        for i in range(max(len(a), len(b))):
            if i < len(a):
                a_bit = int(a[-i-1])
            else:
                a_bit = 0
            if i < len(b):
                b_bit = int(b[-i-1])
            else:
                b_bit = 0


if __name__ == '__main__':
    a = '11'
    b = '1'
    binary = Binary()
    print(binary.addBinary(a, b))

