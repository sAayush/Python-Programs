def threesquares(m):
    for a in range(int(m**0.5)+1):
        for b in range(int(m**0.5)+1):
            for c in range(int(m**0.5)+1):
                if a**2 + b**2 + c**2 == m:
                    return True
    return False


if __name__ == "__main__":
    n = 6
    print(threesquares(n))