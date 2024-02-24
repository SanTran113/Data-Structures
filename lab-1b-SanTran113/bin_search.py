# CPE 202 Lab 1b
from typing import List, Optional

# Binary Search using iteration
# Python List (or None), number -> number or None
def bin_search_iter(int_list: Optional[List], target: int) -> Optional[int]:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    low = 0
    high = len(int_list) - 1
    if high == 0:
        for _ in int_list:
            if _ is target:
                return 0
            else:
                return None
    while low < high:
        mid = (high + low) // 2
        if int_list[mid] < target:  # If mid value is less than target, ignore left half
            low = mid + 1
        elif int_list[mid] > target:  # If mid value is greater than target, ignore right half
            high = mid - 1
        else:  # mid value must equal target
            return mid
    # If we reach here, target not present
    return None

# Binary Search using recursion
# Python List (or None), number -> number or None
def bin_search_rec(int_list: Optional[List], target: int) -> Optional[int]:
    """ searches for target in int_list and returns associated index if found, otherwise returns None
        int_list must be in ascending order for Binary Search to return proper result
        if int_list is None, raise ValueError"""
    if int_list is None:
        raise ValueError
    int_list = sorted(int_list, reverse=False)
    print(int_list)
    return bin_search_rec_helper(int_list, target, 0, len(int_list)-1)

# Recursive helper function
# Python List, number, number, number -> number or None
def bin_search_rec_helper(int_list: List, target: int, low: int, high: int) -> Optional[int]:
    """ searches for target in int_list[low..high] and returns index if found"""
    mid = (high + low) // 2
    if low > high:
        return None
    elif int_list[mid] < target:
        return bin_search_rec_helper(int_list, target, mid + 1, high)
    elif int_list[mid] > target:
        return bin_search_rec_helper(int_list, target, low, mid - 1)
    else:
        return mid


    # if int_list[mid] == target:
    #     return mid
    # elif low == high:
    #     return None
    # elif int_list[mid] > target:
    #     return bin_search_rec_helper(int_list, target, low, mid)
    # else:
    #     return bin_search_rec_helper(int_list, target, mid, high)

    # for _ in newList:
    #     if _ == target:
    #         return newList.index(target)
    #     # return bin_search_rec(newList, target)
    #     return bin_search_rec_helper(int_list, target, newList[0], newList[-1])

    # if target in newList:
    #     return newList.index(target)
    # else:
    #     return None

# print(bin_search_rec_helper([1, 2, 3, 4, 5], 3, 1, 5))