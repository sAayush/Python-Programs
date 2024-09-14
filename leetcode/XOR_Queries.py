class XorQueries:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xor = [0]
        
        for i in range(len(arr)):
            xor.append(xor[-1] ^ arr[i])
            
        res = []
        for l, r in queries:
            res.append(xor[l] ^ xor[r+1])
            
        return res
        
        
    
if __name__ == '__main__':
    xq = XorQueries()
    print(xq.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])) # [2,7,14,8]