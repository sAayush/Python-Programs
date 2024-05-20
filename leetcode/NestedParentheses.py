class NestPare:
    def maxDepth(self, s: str) -> int:
        maxd = 0
        currd = 0
        for c in s:
            if c == '(':
                currd += 1
                maxd = max(maxd, currd)
            elif c == ')':
                currd -= 1
        return maxd


if __name__ == '__main__':
    np = NestPare()
    print(np.maxDepth('(1+(2*3)+((8)/4))+1')) # 3
