# introman.py - integer to roman literals from 1 to 3999
def solution(n):
    def get_digit(number, m):
        return number // 10 ** m % 10

    roman = []
    nlen = len(str(n))
    print(nlen)
    if nlen == 4:
        while n >= 1000:
            n -= 1000
            roman.append('M')
    d = get_digit(n, 2)
    if nlen >= 3 and d != 0:
        switch = {
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM'
        }
        roman.append(switch.get(d))
    d = get_digit(n, 1)
    if nlen >= 2 and d != 0:
        switch = {
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC'
        }
        roman.append(switch.get(d))
    d = get_digit(n, 0)
    if nlen >= 1 and d != 0:
        switch = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
        }
        roman.append(switch.get(d))

    return ''.join(roman)


print(solution(1889))  # outputs MDCCCLXXXIX
