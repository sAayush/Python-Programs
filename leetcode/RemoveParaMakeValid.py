class RemoveParenthesis:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)


if __name__ == '__main__':
    s = "lee(t(c)o)de)"
    rp = RemoveParenthesis()
    print(rp.minRemoveToMakeValid(s))