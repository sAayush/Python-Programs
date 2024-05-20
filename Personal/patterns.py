class pattern:
    def star(self, n):
        for i in range(n):
            print('*' * (i+1))

    def revereseStar(self, n):
        for i in range(n, 0, -1):
            print('*' * i)

    def nums(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end=' ')
            print()

    def numsContinue(self, n):
        c = 0
        for i in range(n):
            for j in range(i+1):
                c += 1
                print(c, end=' ')
            print()

    def rectangle(self, l, b):
        print('*' * l)
        for i in range(l):
            print('*', ' ' * (b-2), '*')
        print('*' * l)


if __name__ == '__main__':
    p = pattern()
    p.star(5)
    print()
    p.revereseStar(5)
    print()
    p.nums(5)
    print()
    p.numsContinue(5)
    print()
    p.rectangle(5, 3)
    