# Algorithms and Data Structures Tutorial - Full Course for Beginners
# https://www.youtube.com/watch?v=8hly31xKli0

testing_list = [1, 2, 3, 4, 5, 6, 7, 8]


def linear_search(arr: list, target: any) -> int:
    """Returns the index position of the target, else -1."""
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def test_search_algorithm(arr: list, target: any, function):
    """
    Function is used solely for testing algorithms.
    It takes as an input a list and a target (element you want to find in the list).
    """
    index = function(arr, target)

    if index != -1:
        result = f"{function.__name__}: Found the target at {index}."
    else:
        result = f"{function.__name__}: Could not find the target. ):"

    # To prevent function from printing 'None'.
    # I hate it.
    return result


def binary_search(lst: list, target: any) -> int:
    """
    Implementation of a binary search algorithm. Takes in a list and a target value.
    """

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # If not found


def recursive_binary_search_for_numbered_list(lst: list, target: any) -> int:
    """
    This function would not work for any other type, except numbers.
    """

    if len(lst) == 0:
        return -1

    midpoint = len(lst) // 2

    if lst[midpoint] == target:
        return midpoint
    elif lst[midpoint] < target:
        right_result = recursive_binary_search_for_numbered_list(
            lst[midpoint + 1 :], target
        )

        if right_result == -1:
            return -1
        else:
            return midpoint + 1 + right_result
    else:
        return recursive_binary_search_for_numbered_list(lst[:midpoint], target)


# Test the functions
print(test_search_algorithm(testing_list, 8, binary_search))  # Using binary search
print(
    test_search_algorithm(testing_list, 8, recursive_binary_search_for_numbered_list)
)  # Using recursive binary search
