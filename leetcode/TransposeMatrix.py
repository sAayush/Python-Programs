class Transpose:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for i in range(len(matrix[0])):
            res.append([])
            for j in range(len(matrix)):
                res[i].append(matrix[j][i])
        return res

if __name__ == '__main__':
    transpose = Transpose()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose.transpose(matrix))