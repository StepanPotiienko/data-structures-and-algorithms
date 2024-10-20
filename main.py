# Algorithms and Data Structures Tutorial - Full Course for Beginners
# https://www.youtube.com/watch?v=8hly31xKli0

def linear_search(arr: list, target): 
    """ Returns the index position of the target, else None. """

    for index in range(0, len(arr)):
        if arr[index] == target:
            return index

    return None
