from collections import Counter

class LeastNumberUniqInts:
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        c = sorted(c.items(), key=lambda x: x[1])
        for i in range(k):
            c[0] = (c[0][0], c[0][1] - 1)
            if c[0][1] == 0:
                c.pop(0)
        return len(c)


if __name__ == "__main__":
    lnqi = LeastNumberUniqInts()
    print(lnqi.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))  # 2
