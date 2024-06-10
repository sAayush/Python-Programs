class HeightChecker:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        
        return count

if __name__ == '__main__':
    hc = HeightChecker()
    print(hc.heightChecker([1,1,4,2,1,3]))      