class ColAplha:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        result.reverse()
        return "".join(result)

if __name__ == "__main__":
    ca = ColAplha()
    print(ca.convertToTitle(1)) # A
    print(ca.convertToTitle(28)) # AB`