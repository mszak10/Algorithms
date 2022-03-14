# petethebaker.py - given the recipe check how many cakes can you make with available resources
from math import floor


def cakes(recipe, available):
    m = None
    for k, v in recipe.items():
        if k not in available.keys():
            return 0
        if m is None or available[k] / recipe[k] < m:
            m = available[k] / recipe[k]
    return floor(m)


r = {"flour": 500, "sugar": 200, "eggs": 1}
a = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(r, a))
