class SequenDigits:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        for i in range(1, 9):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)

        # c = "123456789"
        # res = []
        #
        # for i in range(9):
        #     for j in range(i + 1, 10):
        #         curr = int(c[i:j])
        #         if low <= curr <= high:
        #             res.append(curr)

        res.sort()
        return res


if __name__ == '__main__':
    sd = SequenDigits()
    print(sd.sequentialDigits(100, 300))  # [123, 234]
