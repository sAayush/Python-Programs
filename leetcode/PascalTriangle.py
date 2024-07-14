class Pascal:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([1] * (i + 1))
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
    
    
if __name__ == "__main__":
    p = Pascal()
    print(p.generate(5))
    