class isPowerOfTwo:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

        # # Brute force

        # for i in range(32):
        #     if 2 ** i == n:
        #         return True
        # return False


if __name__ == "__main__":
    ipt = isPowerOfTwo()
    print(ipt.isPowerOfTwo(16))  # True