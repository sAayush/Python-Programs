class IntBreak:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        remainder = n % 3
        quotient = n // 3

        if remainder == 0:
            return 3 ** quotient
            # if n = 9 then it will the reminder will be 0 and the quotient will be 3
            # so it will return 3 ** 3 = 27
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
            # if n = 10 then the remainder will be 1 and the quotient will be 3
            # and 1 * anything is just that number so we can't do 3 ** 3 * 1
            # so we have to do 3 ** 2(2 because 3-1) * 4
        else:
            return 3 ** quotient * 2
            # if n = 11 then the remainder will be 2 and the quotient will be 3
            # so we can do 3 ** 3 * 2

if __name__ == "__main__":
    obj = IntBreak()
    print(obj.integerBreak(10))