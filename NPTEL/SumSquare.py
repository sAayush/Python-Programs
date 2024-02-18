def sumsquare(l):
    evensum = 0
    oddsum = 0
    for i in l:
        if i % 2 == 0:
            evensum += i ** 2
        else:
            oddsum += i ** 2
    return [oddsum, evensum]


if __name__ == '__main__':
    print(sumsquare([-1, -2, 3, 7]))  # [59, 4]
