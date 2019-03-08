vals = {'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1}


def romantoint(str):
    total = 0
    for i in range(0, len(str)-1):
        if vals[str[i]] < vals[str[i+1]]:
            total -= vals[str[i]]
        else:
            total += vals[str[i]]

    return total+vals[str[-1]]


print(romantoint('IX'))

# Runtime: 152 ms, faster than 35.30 % of Python3 online submissions
# Memory Usage: 13.3 MB, less than 5.05 % of Python3 online submissions

# if in string the alphabet's value is smaller than that of next
# alphabet, we subtract from total else we add

# todo:
# something faster
