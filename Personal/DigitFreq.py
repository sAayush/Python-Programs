class DegitFreq:
    def OneToTen(self, num : int) -> int:
        freq = [0] * 10
        while num > 0:
            freq[num % 10] += 1
            num //= 10
        return freq