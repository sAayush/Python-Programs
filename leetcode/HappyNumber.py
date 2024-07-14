class HappyNumber:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            total_sum = 0
            while n > 0:
                # print(n)
                n, digit = divmod(n, 10)
                # print(n, digit)
                total_sum += digit ** 2
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            # print(n)
            # print(seen)
            n = get_next(n)
        return n == 1
    

if __name__ == "__main__":
    hn = HappyNumber()
    print(hn.isHappy(19)) # True