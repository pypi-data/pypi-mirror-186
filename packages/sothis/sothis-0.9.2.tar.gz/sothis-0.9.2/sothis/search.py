"""
Name: search.py
Author: Oliver B. Gaither
Date:
Description:
"""

def binarysearch(data, target):
    """
    basic binary search function for
    a given existing sorted dataset and target
    :param data: sorted indexable collection
    :param target: search query
    :return: True or False
    """
    
    lo = 0
    hi = len(data) - 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if data[mid] == target:
            return True
        elif target < data[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


