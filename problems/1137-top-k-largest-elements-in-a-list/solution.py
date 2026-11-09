import heapq

def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    return heapq.nlargest(3, values)