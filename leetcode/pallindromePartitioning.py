class PallinPartition:
    def partition(self, s: str) -> list[list[str]]:
        def isPallin(s):
            return s == s[::-1]

        result = []

        # this backtrack function does the task
        # of finding all the pallindromic partitions
        # of the string s
        # start is the index from where we start
        # path is the current partition

        def backtrack(start, path):
            if start == len(s): # when we reach the end of the string
                result.append(path)
                return
            for i in range(start, len(s)):
                if isPallin(s[start:i+1]):
                    backtrack(i+1, path + [s[start:i+1]]) # we add the current pallindromic partition to the path
        backtrack(0, [])
        return result


if __name__ == '__main__':
    pp = PallinPartition()
    print(pp.partition("aab"))


