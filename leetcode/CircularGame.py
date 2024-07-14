class CircularGame:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        return (self.findTheWinner(n - 1, k) + k - 1) % n + 1
        
        
        
    

if __name__ == "__main__":
    cg = CircularGame()
    print(cg.findTheWinner(5, 2)) # 3
    print(cg.findTheWinner(6, 5)) # 1
    print(cg.findTheWinner(10, 17)) # 2