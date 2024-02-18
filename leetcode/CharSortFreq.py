class FreqCharSort:
    def frequencySort(self, s: str) -> str:
        # Using dictionary

        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        s = ''
        for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
            s += k * v
        return s


if __name__ == '__main__':
    fcs = FreqCharSort()
    print(fcs.frequencySort("tree"))  # eert
    print(fcs.frequencySort("cccaaa"))  # cccaaa
    print(fcs.frequencySort("Aabb"))  # bbAa
