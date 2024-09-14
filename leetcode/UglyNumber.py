class Ugly:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for i in [2, 3, 5]:
            while n % i == 0:
                n /= i
            
        return n == 1
    

if __name__ == '__main__':
    u = Ugly()
    print(u.isUgly(6)) # True