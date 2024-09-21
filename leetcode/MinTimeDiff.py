class MinTimeDiff:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []
        res = float('inf')
        
        for time in timePoints:
            h, m = time.split(":")
            minutes.append(int(h) * 60 + int(m))
            
        minutes.sort()
        for i in range(1, len(minutes)):
            res = min(res, minutes[i] - minutes[i-1])
        
        res = min(res, 1440 - minutes[-1] + minutes[0])
        return res
        
    
if __name__ == '__main__':
    test = MinTimeDiff()
    print(test.findMinDifference(["23:59","00:00"])) # 1
    print(test.findMinDifference(["00:00","23:59","00:00"])) # 0