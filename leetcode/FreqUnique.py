class Freq:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = [0] * 2001
        for i in range(len(arr)):
            count[arr[i] + 1000] += 1
        # print(count)
        count.sort()

        for i in range(1, len(count)):
            if count[i] == count[i - 1] and count[i] != 0:
                return False
        return True


if __name__ == "__main__":
    F = Freq()
    arr = [1, 2, 2, 1, 1, 3]
    print(F.uniqueOccurrences(arr))
