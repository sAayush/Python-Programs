class Multi:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    m = Multi()
    print(m.multiply("123", "456"))