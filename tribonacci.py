# tribonacci.py - fibonacci, but sum last three digits
def tribonacci(signature, n):
    for i in range(n-3):
        signature.append(sum(signature[i:i+3]))
    return signature[:n]


print(tribonacci([1, 1, 1], 10))  # outputs [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
