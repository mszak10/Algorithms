# permutations.py -  create all permutations of a non empty input string and remove duplicates
import itertools


def permutations(string):
    perm = list(itertools.permutations(string))
    r = []
    for i in range(len(perm)):
        retstr = ''
        for j in range(len(string)):
            retstr += perm[i][j]  # PURPOSE: [a,b,c] -> [abc]
        r.append(retstr)

    return list(set(r))  # PURPOSE: removes non-unique values and returns


print(permutations("aabb"))  # outputs ['bbaa', 'abba', 'baba', 'abab', 'baab', 'aabb']
