# lastDigitLargeNumber.py - Function that takes in two non-negative integers a and b
#                           and returns the last decimal digit of a^b
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    switch = {  # PURPOSE: key is last digit of n1, value is the pattern of last digits of the result
        0: [0],
        1: [1],
        2: [4, 8, 6, 2],
        3: [9, 7, 1, 3],
        4: [6, 4],
        5: [5],
        6: [6],
        7: [9, 3, 1, 7],
        8: [4, 2, 6, 8],
        9: [1, 9]
    }

    n1str = str(n1)
    if len(n1str) != 1:
        n1str = str(n1str[-1:])  # PURPOSE: if more than 1 digit, get only the last one
    lastnumlist = switch.get(int(n1str))

    index = n2 % len(lastnumlist) - 2
    if index < 0:
        index += len(lastnumlist)
    return lastnumlist[index]


print(last_digit(3715290469715693021198967285016729344580685479654510946723,
                 68819615221552997273737174557165657483427362207517952651))
# outputs 7
