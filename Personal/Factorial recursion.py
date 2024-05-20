class RecursionFact:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


if __name__ == '__main__':
    rf = RecursionFact()
    data = int(input('Enter a number: '))
    print(rf.factorial(data))