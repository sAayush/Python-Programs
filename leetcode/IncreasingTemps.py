class Increasing:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                result[cur] = i - cur
            stack.append(i)
        return result


if __name__ == '__main__':
    i = Increasing()
    print(i.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
