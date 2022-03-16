# anagram.py - find all the anagrams of a word from a list
def anagrams(word, words):
    retlist = []  # return list
    sword = sorted(word)  # sorted word
    for w in words:
        if sorted(w) == sword:
            retlist.append(w)
    return retlist


# Different approach:

def anagrams_faster(word, words): return [w for w in words if sorted(w) == sorted(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # executed in 0.0000220s
print(anagrams_faster('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # executed in 0.0000094s
# both output ['aabb', 'bbaa']
# ============================
# anagrams_faster() is faster by 42,72%
#
# Measured by:
# import decimal
# from timeit import default_timer as timer
# start = timer()
# print(anagrams_faster('abba', ['aabb', ....]))
# end = timer()
# print(decimal.Decimal(end - start))
