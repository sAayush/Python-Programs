class RevBits:
    def reverseBits(self, n: int) -> int:
        # it works because we are using 32 bits
        # we can use a mask to get the last bit of n
        # and then shift n to the right
        # and shift rev to the left
        # then we add the last bit of n to rev
        # and repeat the process
        
        rev = 0
        for i in range(32):
            rev = rev << 1
            if n & 1:
                rev = rev | 1
            n = n >> 1
        return rev
    
    

if __name__ == "__main__":
    rb = RevBits()
    print(rb.reverseBits(11001)) # 964176192