class ArrMax:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        size = len(arr)
        arr.sort()
        max_sum = 0
        curr_index = 0
        for i in range(-1, -size, -1):
            if curr_index + k < size:
                max_sum += arr[i] * k
                curr_index += k
                # print(max_sum, curr_index, size, arr[i])

            else:
                max_sum += arr[i] * (size - curr_index)
                # print(max_sum, curr_index, size, arr[i])
                break

        return max_sum


if __name__ == '__main__':
    arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 3
    print(ArrMax().maxSumAfterPartitioning(arr, k))