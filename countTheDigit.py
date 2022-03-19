# countTheDigit.py - square all numbers between 0 and n
#                    return how many times 'd' digit occurs in 'n'

def nb_dig(n, d):
    ret = 0  # PURPOSE: counter
    for i in range(n+1):
        r = i ** 2
        for char in str(r):
            if char == str(d):  # PURPOSE: for each digit check if it matches d
                ret += 1
    return ret


print(nb_dig(25, 1))  # returns 11
