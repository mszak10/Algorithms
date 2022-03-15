# rangeExtraction.py - TBD
# TODO not finished: moving to different device

def solution(n):
    dist = {}
    ret = []
    for i, val in enumerate(n):
        print(f'{i}: {abs(n[i]-n[i+1])}')

    return ''.join(ret)


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
