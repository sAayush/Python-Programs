class BitwiseAND:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right - 1)
        return right


if __name__ == "__main__":
    bw = BitwiseAND()
    print(bw.rangeBitwiseAnd(5, 7))  # 4
