class Choco:
    def buyChoco(self, prices: list[int], money: int) -> int:
        first_min_cost = second_min_cost = float("inf")

        for p in prices:
            if p < first_min_cost:
                second_min_cost, first_min_cost = first_min_cost, p
            else:
                second_min_cost = min(second_min_cost, p)

        leftover = money - (first_min_cost + second_min_cost)

        return leftover if leftover >= 0 else money


if __name__ == "__main__":
    ch = Choco()
    price = [1, 2, 2]
    money = 3
    print(ch.buyChoco(price, money))
