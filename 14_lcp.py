def lcp(arr):
    n = len(arr)
    result = ''
    if n == 0:
        return result
    minlen = len(min(arr, key=len))


# minlen will give error if there is an empty string in list
# so added condition for empty string

    for i in range(minlen):
        current = arr[0][i]
        for j in range(1, n):
            if(arr[j][i] != current):
                return result
# result moved to outer for loop because current  was
# getting added twice to result inside inner for loop
        result += current
    return result


print(lcp(['flight', 'flow', 'flower']))

# algorithm:
# find the len of minimum string in the list
# for this min length
# compare character by character the first string to all
# first loop is for 1st word
# 2nd loop is for strings from index 2 to last
# if they all match add to result variable
# if they dont return result


# Runtime: 44 ms, faster than 47.64% of Python3
# Memory Usage: 13.1 MB, less than 5.10% of Python3
