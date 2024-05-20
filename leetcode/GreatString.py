class GrtString:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    s = "leEeetcode"
    gs = GrtString()
    print(gs.makeGood(s))