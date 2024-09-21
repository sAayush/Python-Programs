def transform_string(s):
    res = ''
    for c in s:
        if c.isupper():
            res += '_'
        elif c.isdigit():
            res += '*'
        else:
            res += c
    return res


# def transform_string(s):
#     return ''.join('_' if char.isupper() else '*' if char.isdigit() else char for char in s)

input_str = "aayUSH1sha23"
output_str = transform_string(input_str)
print(output_str) 