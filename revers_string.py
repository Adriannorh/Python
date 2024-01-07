#str[start:stop:step]

trail = "reversal"
new_trail = trail[::-1]
print(new_trail)


# # str reverse 2

def strign_reverse(str):
    if len(str) == 0:
        return str
    else:
        return strign_reverse(str[1:]) + str[0]

str = "Python"
reverse = strign_reverse(str)
print(reverse)