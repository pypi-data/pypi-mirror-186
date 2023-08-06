"""
Name: helpers.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: misc. helper functions
"""

import time as ti # perf_counter_ns() count nanoseconds

def print_list(x, char=''):
    """
    prints a list with an option list dot
    :param x:
    :param char:
    :return:
    """
    for el in x:
        print(f"{char}{el}")

def isint(n):
    """
    returns whether a given value is a valid integer
    :param n: some value
    :return: boolean whether n is a whole number
    """
    try:
        x = float(n)  # attempt conversion of ascii to float
        if x % 1 != 0:  # check if input is a whole number by mod by 1
            return False
        return True
    except ValueError:
        return False


def isfloat(n):
    """
    returns whether a given value is a valid integer
    :param n: some value
    :return: boolean whether n is a whole number
    """
    try:
        x = float(n)  # attempt conversion of ascii to float
        return True
    except ValueError:
        return False


def runtime(func):
    """decorator function to measure the time take to execute a function on your machine"""
    
    def wrapper(*args, **kwargs):
        start = ti.perf_counter_ns()
        result = func(*args, **kwargs)
        end = ti.perf_counter_ns()
        extension = "ns"
        length = (end - start)
        if (length >= 1e9):
            extension = "s"
            length /= 1e9
        elif (length >= 1e6):
            extension = "ms"
            length /= 1e6
        
        print('{} runtime: {}{}'.format(
            func.__name__, length, extension
        ))
        return result
    
    return wrapper

