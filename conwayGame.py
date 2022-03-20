# conwayGame.py - gets next generation of Conway's Game of Life
# Almost finished - TODO make sure all tests are green
import numpy as np


def next_gen(cells):
    rowlen = len(cells)
    collumnlen = len(cells[0])
    rettab = []

    surrounding = [
        [1, -1, -1],
        [2, -1, 0],
        [3, -1, 1],
        [3, 0, -1],
        [4, 0, 1],
        [5, 1, -1],
        [6, 1, 0],
        [7, 1, 1]
    ]

    def check_for_adj():
        tab = []
        tabb = []
        for r in range(rowlen):
            try:
                for c in range(collumnlen):  # PURPOSE: iteration through all cells
                    try:
                        # print(r, c)  # DEBUG
                        count = 0
                        for i in range(len(surrounding)):
                            try:
                                if r + surrounding[i][1] < 0 or c + surrounding[i][2] < 0:
                                    continue
                                if cells[r + surrounding[i][1]][c + surrounding[i][2]] == 1:
                                    # print('if i=', i, cells[r][c], cells[r + surrounding[i][1]][c + surrounding[i][2]])
                                    count += 1
                            except IndexError:
                                continue
                        tab.append(count)
                    except IndexError:
                        continue
                    # print(count)

            except IndexError:
                continue
        tabb = np.reshape(tab, (rowlen, collumnlen))
        print(tab)
        print(tabb)
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

    print(cells)

    adj = check_for_adj()

    booltab = []
    for a in range(len(adj)):
        for b in range(len(adj[0])):
            booltab.append(boolify(adj[a][b]))

    booltab2d = np.reshape(booltab, (rowlen, collumnlen))
    print(booltab2d)

    for i in range(len(booltab2d)):
        for j, v in enumerate(booltab2d[i]):
            if v is False:
                rettab.append(0)
                continue
            elif v:
                rettab.append(1)
                continue
            else:
                rettab.append(cells[i][j])

    print(rettab)
    return np.reshape(rettab, (rowlen, collumnlen))


print(next_gen([[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]))
# DEBUG:       [[0, 0, 0],
#               [1, 1, 1],
#               [0, 0, 0]]
