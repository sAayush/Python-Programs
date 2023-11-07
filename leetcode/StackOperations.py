class StackOps:
    @staticmethod
    def buildArray(target: list[int], n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            if i in target:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
            if i == target[-1]:
                break
        return res

    # def buildArray(self, target, n):
    #     res = []
    #     curr = 1
    #     for n in target:
    #         while curr < n:
    #             res.extend(["Push", "Pop"])
    #             curr += 1
    #         res.append("Push")
    #         curr += 1
    #     return res


if __name__ == '__main__':
    stackOps = StackOps()
    target = [1, 3]
    n = 3
    print(stackOps.buildArray(target, n))

