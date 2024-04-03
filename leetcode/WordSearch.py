class WordSear:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board: list[list[str]], i: int, j: int, word: str) -> bool:
        # if the word is empty, return True
        if len(word) == 0:
            return True
        # if the index is out of bounds or the first letter of the word is not the same as the letter at the index, return False
        # if the letter at the index is the same as the first letter of the word, set the letter at the index to '#' and store the letter in a temporary variable
        # because we need to change the letter back to the original letter after the dfs call
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        # if the letter at the index is the same as the first letter of the word, set the letter at the index to '#' and store the letter in a temporary variable
        # because we need to change the letter back to the original letter after the dfs call
        tmp, board[i][j] = board[i][j], '#'
        # recursively call the dfs function with the updated board, the next index and the rest of the word
        # if any of the recursive calls return True, return True
        # if all of the recursive calls return False, change the letter back to the original letter and return False
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        # change the letter back to the original letter
        board[i][j] = tmp
        return res


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    ws = WordSear()
    print(ws.exist(board, word)) # True