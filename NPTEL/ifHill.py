def hillvalley(l):
    if len(l) < 3:
        return False
    if l[0] < l[1]:
        inc = True
    else:
        inc = False
    for i in range(1, len(l)):
        if inc and l[i-1] > l[i]:
            inc = False
        elif not inc and l[i-1] < l[i]:
            return False
    return True


if __name__ == '__main__':
    print(hillvalley([1, 3, 5, 2, 1]))
    print(hillvalley([1, 3, 5, 3, 1]))
    print(hillvalley([1, 3, 5, 4, 1]))
    print(hillvalley([1, 3, 5, 5, 1]))
    print(hillvalley([1, 3, 5, 6, 1]))

