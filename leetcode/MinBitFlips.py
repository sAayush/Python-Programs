class BitFlipComapare:
    def minBitFlips(self, start: int, goal: int) -> int:
        # start = list(map(int, bin(start)[2:]))
        # goal = list(map(int, bin(goal)[2:]))
        # res = 0
        # print(len(start), len(goal))
        # print(start, goal)
        # if len(start) > len(goal):
        #     for i in range(len(start) - len(goal)):
        #         goal.insert(0, 0)
            
            
        # if len(goal) > len(start):
        #     for i in range(len(goal) - len(start)):
        #         start.insert(0, 0)
                
        # print(start, goal)
        
        # for i in range(len(start)):
        #     if start[i] != goal[i]:
        #         res += 1
        
        # return res
        
        count = 0
        while start or goal:
            if start % 2 != goal % 2:
                count += 1
            start //= 2
            goal //= 2
            
        return count

if __name__ == '__main__':
    start = 7
    goal = 10
    bfc = BitFlipComapare()
    print(bfc.minBitFlips(start, goal))