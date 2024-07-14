class WaterBottles:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # this method is based on the fact that we can exchange numExchange empty bottles for 1 full bottle
        # so we can keep exchanging until we have less than numExchange empty bottles
        
        # numBottles + (numBottles - 1) // (numExchange - 1) is the formula to calculate the total number of bottles
        # numBottles is the number of full bottles we have
        # numBottles - 1 is the number of empty bottles we have
        # numExchange - 1 is the number of empty bottles we need to exchange for 1 full bottle
        # (numBottles - 1) // (numExchange - 1) is the number of full bottles we can get from the empty bottles
        # numBottles + (numBottles - 1) // (numExchange - 1) is the total number of bottles we can get

        # return numBottles + (numBottles - 1) // (numExchange - 1)
    
        # we can also use the following code to achieve the same result
        
        empty = 0
        total = 0
        while numBottles > 0:
            total += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return total
    


if __name__ == '__main__':
    p = 15
    q = 4
    s = WaterBottles()
    print(s.numWaterBottles(p, q))