class MinOdd:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count1 = s.count('1')
        count0 = s.count('0')
        if count1 == 0:
            return s
        return '1' * (count1 - 1) + '0' * count0 + '1'


if __name__ == '__main__':
    s = MinOdd()
    print(s.maximumOddBinaryNumber("010"))
