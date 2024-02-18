def remdup(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


if __name__ == '__main__':
    print(remdup([1, 2, 2, 3, 4, 4, 4, 5, 5]))  # [1, 2, 3, 4, 5]
