class BinToOne:
    def numSteps(self, s: str) -> int:
        # it works because the number of steps is the number of 1s in the string
        # plus the number of 0s in the string except the last one
        # plus 1 if there is a carry
        
        n = len(s)
        steps = 0
        carry = 0
        for i in range(n - 1, 0, -1):
            if s[i] == '1':
                carry = 1
                steps += 2
            else:
                steps += 1
            if carry == 1:
                steps += 1
        return steps + carry
    

if __name__ == '__main__':
    bto = BinToOne()
    print(bto.numSteps("1101"))  # 6
    print(bto.numSteps("10"))  # 1