class RelativeSort:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    res.append(arr1[j])
                    arr1[j] = -1

        arr1.sort()
        for i in range(len(arr1)):
            if arr1[i] != -1:
                res.append(arr1[i])
        return res


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    relative_sort = RelativeSort()
    print(relative_sort.relativeSortArray(arr1, arr2))
