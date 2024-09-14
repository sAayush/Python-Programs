class Obervations:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        total = mean * (len(rolls) + n)
        rollSum = sum(rolls)
        remainingTotal = total - rollSum
        if remainingTotal < n or remainingTotal > 6 * n:
            return []
        
        res = [remainingTotal // n] * n
        
        for i in range(remainingTotal % n):
            res[i] += 1
        return res
    
    

if __name__ == '__main__':
    obj = Obervations()
    print(obj.missingRolls([3,2,4,3], 4, 2)) # [6,6]
    