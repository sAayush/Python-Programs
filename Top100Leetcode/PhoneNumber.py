def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    res = ['']
    for digit in digits:
        # it works by iterating over the digits and for each digit, it iterates over the letters
        # and for each letter, it adds the letter to the previous result
        # when the res is empty at start it adds an empty string to it
        # then it iterates over the letters of the first digit and assigns each letter to the empty string
        # Rather then adding it rather just changes the whole value so it just overrides the past one

        res = [prev + letter for prev in res for letter in mapping[digit]]
    return res


if __name__ == '__main__':
    digits = "232"
    print(letterCombinations(digits))
