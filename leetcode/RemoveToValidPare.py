class MakeValidParenthesis:
    def minRemoveToMakeValid(self, s: str) -> str:
# this works because it uses a stack to keep track of the indices of the open parentheses and a set to keep track of the indices of the parentheses that need to be removed
        # if the character is an open parenthesis, add the index to the stack
        # if the character is a close parenthesis, check if the stack is empty
        # if the stack is empty, add the index to the set
        # if the stack is not empty, pop the index from the stack
        # if the set is not empty, add the indices to the set
        # return the string with the indices removed
        stack = []
        remove = set()
        for i, c in enumerate(s):
            print(i, c, stack, remove)
            if c == '(':
                stack.append(i)
            elif c == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()
        remove = remove.union(set(stack))
        return ''.join(c for i, c in enumerate(s) if i not in remove)


if __name__ == '__main__':
    mvp = MakeValidParenthesis()
    print(mvp.minRemoveToMakeValid('lee(t(c)o)de)'))  # lee(t(c)o)de
    print(mvp.minRemoveToMakeValid('a)b(c)d'))  # ab(c)d
    print(mvp.minRemoveToMakeValid('))(('))  # ''
    print(mvp.minRemoveToMakeValid('(a(b(c)d)'))  # a(b(c)d)