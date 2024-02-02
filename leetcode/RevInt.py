class Rev:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x # this line makes the number positive
            x = str(x)
            x = x[::-1] # this line reverses the string by slicing it backwards
            x = int(x)
            x = -x # this line makes the number negative again
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        else:
            return x


if __name__ == '__main__':
    r = Rev()
    print(r.reverse(123))
    print(r.reverse(120))
