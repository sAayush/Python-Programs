class Paranthesis:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(len(expression)):
            if expression[i] in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.helper(l, r, expression[i]))
        return res
    
    def helper(self, a: int, b: int, op: str) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            return a * b
        


if __name__ == '__main__':
    p = Paranthesis()
    print(p.diffWaysToCompute('2-1-1'))