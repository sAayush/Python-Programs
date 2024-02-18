def repfree(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return False
    return True


if __name__ == "__main__":
    print(repfree("noor"))  # False
    print(repfree("abcd"))  # True
    print(repfree("abba"))  # False
