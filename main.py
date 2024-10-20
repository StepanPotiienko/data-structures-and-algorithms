# Algorithms and Data Structures Tutorial - Full Course for Beginners
# https://www.youtube.com/watch?v=8hly31xKli0


testing_list = [1, 2, 3, 4, 5, 6, 7, 8]


def linear_search(arr: list, target): 
    """ Returns the index position of the target, else None. """

    for index in range(0, len(arr)):
        if arr[index] == target:
            return index

    return None


def test_search_algorithm(arr: list, target, function):
    """ 
    Function is used solely for testing algorithms.
    It takes as an input a list and a target (element you want to find in the list). 
    """

    index = function(arr, target)

    if index is not None:
        print(f'Found the target at {index}.')
    else:
        print("Could not find the target. ):")



def binary_search(list, target):
    """
    Implementation of a binary search algorithm. Takes in a list and a target value.
    """
    start = 0 
    end = len(list) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if list[mid] == target:
            return mid
        
        elif list[mid] < target:
            start = mid + 1

        else:
            end = mid - 1


    else:
        return None

print(test_search_algorithm(testing_list, 8, binary_search))
