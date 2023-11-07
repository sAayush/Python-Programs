def check(word):
    alphas = [0] * 26
    for i in range(len(word)):
        alphas[word(i) - 'a'] += 1

    print(alphas)
    # for i in len(alphas):
    #     if alphas[i] == 0:
    #         return False


def find():
    pass


word = str(input("Enter a string: "))
check(word)
