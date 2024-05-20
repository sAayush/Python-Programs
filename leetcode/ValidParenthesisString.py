class ValidParenString:
    def checkValidString(self, s: str) -> bool:
        # this works because it uses two counters to keep track of the minimum and maximum number of open parentheses
        # if the maximum number of open parentheses is less than 0, return False
        # if the minimum number of open parentheses is greater than 0, return False
        # if both of the conditions are met, return True
        minop = maxop = 0
        for c in s:
            minop += 1 if c == '(' else -1
            maxop += 1 if c != ')' else -1
            if maxop < 0:
                return False
            minop = max(0, minop)
        return minop == 0


if __name__ == '__main__':
    vps = ValidParenString()
    print(vps.checkValidString('()'))  # True
    print(vps.checkValidString('(*)'))  # True
    print(vps.checkValidString('(*))'))  # True
    print(vps.checkValidString(')('))  # False
    print(vps.checkValidString('((**'))  # True
