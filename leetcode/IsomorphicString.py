class IsoString:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # this works because it checks if the length of the set of s, t and the zipped s and t are the same
        # zip returns a list of tuples where the i-th tuple contains the i-th element from each of the argument sequences or iterables
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == '__main__':
    isos = IsoString()
    print(isos.isIsomorphic('egg', 'add')) # True
    print(isos.isIsomorphic('foo', 'bar')) # False
    print(isos.isIsomorphic('paper', 'title')) # True
    print(isos.isIsomorphic('ab', 'aa')) # False
