def differenceofSum(n, m):
    # sum1=0
    # sum2=0
    # for i in range(1,m+1):
    #     if i%n==0:
    #         sum1+=i
    #     else:
    #         sum2+=i
    # return sum2-sum1
        
    nreal = n
    arr = []
    while nreal <= m:
        arr.append(nreal)
        nreal += n
        
    n = 0
    for i in range(1, m+1):
        if i not in arr:
            n += i
    
    return n - sum(arr)
    


if __name__ == "__main__":
    print(differenceofSum(4, 20)) # 90