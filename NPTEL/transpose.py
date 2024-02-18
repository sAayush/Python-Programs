def transpose(m):
    # this works by taking the first element of each row and putting it into a new row
    # then the second element of each row and putting it into a new row and so on
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m))