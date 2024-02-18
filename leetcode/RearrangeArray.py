class AlternatePositiveNegative:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        result = []
        i = 0
        j = 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        return result


if __name__ == "__main__":
    apn = AlternatePositiveNegative()
    print(apn.rearrangeArray([3, 1, -2, -5, 2, -4])) # [3, -2, 1, -5, 2, -4]
