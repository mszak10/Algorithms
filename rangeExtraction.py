# rangeExtraction.py - for 3 or more consequitve integers create a range
# [1, 3, 4, 5, 6, 8] -> [1, 3-6, 8]

def solution(n):
    retlist = []  # return list
    j = 0
    for i, val in enumerate(n):
        if j != 0:  # PURPOSE: for is skipped j times
            j -= 1
            continue
        start = 0  # PURPOSE: removes a warning (referece before assignment)
        try:
            if abs(n[i] - n[i + 1]) == 1:
                start = val  # PURPOSE: start of range
                i += 1
                if abs(n[i] - n[i + 1]) == 1:
                    i += 1
                    j += 1
                    if i + 1 == len(n):  # PURPOSE: removes duplicate element of list
                        end = n[i]
                        retlist.append(f'{start}-{end},')
                        break
                    while abs(n[i] - n[i + 1]) == 1:
                        i += 1
                        j += 1
                        if i + 1 == len(n):  # PURPOSE: removes duplicate element of list
                            break
                    end = n[i]  # PURPOSE: end of range
                    j += 1
                    retlist.append(f'{start}-{end},')
                else:
                    retlist.append(f'{val},')
            else:
                retlist.append(f'{val},')
        except IndexError:
            if abs(n[i - 1] - n[i]) == 1 and abs(n[i - 2] - n[i - 1]) == 1:
                end = i
                retlist.append(f'{start}-{end},')
            else:
                retlist.append(f'{val},')

    retstr = ''  # returned string
    for r in retlist:  # PURPOSE: list of strings to string
        retstr += r

    return retstr[:-1]  # PURPOSE [:-1]: removes last comma


print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# outputs "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
