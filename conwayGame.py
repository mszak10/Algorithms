# conwayGame.py - gets next generation of Conway's Game of Life
# Almost finished - TODO make sure all tests are green
import numpy as np


def next_gen(cells):
    rowlen = len(cells)
    collumnlen = len(cells[0])
    rettab = []

    surrounding = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    def check_for_adj():
        tab = []

        for r in range(rowlen):
            try:
                for c in range(collumnlen):  # PURPOSE: iteration through all cells
                    try:
                        count = 0
                        for x in range(len(surrounding)):
                            try:
                                if r + surrounding[x][0] < 0 or c + surrounding[x][1] < 0:
                                    continue
                                if cells[r + surrounding[x][0]][c + surrounding[x][1]] == 1:
                                    count += 1
                            except IndexError:
                                continue
                        tab.append(count)
                    except IndexError:
                        continue

            except IndexError:
                continue
        tabb = np.reshape(tab, (rowlen, collumnlen))
        print(tabb)  # PURPOSE: number of adjecent live cells
        return tabb

    def boolify(num):  # PURPOSE: None - don't change; True - set to one; False - set to zero
        if num < 2:
            return False
        elif num == 2:
            return None
        elif num == 3:
            return True
        else:
            return False

    print(cells)  # PURPOSE: initial table

    adj = check_for_adj()

    booltab = []
    for a in range(len(adj)):
        for b in range(len(adj[0])):
            booltab.append(boolify(adj[a][b]))

    booltab2d = np.reshape(booltab, (rowlen, collumnlen))
    print(booltab2d)  # PURPOSE: what to change: true = 1, false = 0, none = keep the value

    for i in range(len(booltab2d)):
        for j, v in enumerate(booltab2d[i]):
            if v is False:  # ERROR this seems not to work in py 3.8, but it works in 3.9
                # TODO research the problem The truth value of an array with more than one element is ambiguous.
                #  Use a.any() or a.all(). This might be codewars specific problem
                rettab.append(0)  # PURPOSE: if the value in booltab2d is False, set to 0
                continue
            elif v:
                rettab.append(1)  # PURPOSE: if the value in booltab2d is True, set to 1
                continue
            else:
                rettab.append(cells[i][j])  # PURPOSE: otherwise, get the valfrom initial table

    return np.reshape(rettab, (rowlen, collumnlen))


print(next_gen([[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]))
# DEBUG:       [[0, 0, 0],
#               [1, 1, 1],
#               [0, 0, 0]]
