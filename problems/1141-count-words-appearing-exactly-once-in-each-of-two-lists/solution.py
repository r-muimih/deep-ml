from collections import Counter

def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    c1, c2 = Counter(list1), Counter(list2)
    return sum(1 for s in c1 if c1[s] == 1 and c2[s] == 1)