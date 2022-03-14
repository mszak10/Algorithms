# movezeros.py - moves all the zeros to the end, preserving the order of the other elements
def move_zeros(array):
    a = []
    print(array.count(0))
    for arr in array:
        if arr != 0:
            a.append(arr)
    for i in range(array.count(0)):
        a.append(0)
    return a


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # outputs [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
