class Most:
    def findSpecialInteger(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        else:
            qtr = len(arr) // 4
            count = 1
            for i in range(1, len(arr) - 1):
                if arr[i] == arr[i + 1]:
                    count += 1
                    if count > qtr:
                        return arr[i]
                else:
                    count = 1
            return arr[0]

        # threshold = len(arr) // 4
        #
        # for i in range(len(arr)):
        #     if arr[i] == arr[i + threshold]:
        #         return arr[i]
        #
        # return -1


if __name__ == '__main__':
    most = Most()
    digits = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(most.findSpecialInteger(digits))

