#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'perfomOperation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY arr
#  2. 2D_INTEGER_ARRAY operations

def performOperations(arr, list_operations):
    """Calculate how many steps you need for your target 
    
    Parameters
    ----------
    arr : list
    list_operationn : list

    Returns:
    --------
    arr : list
    """
    # build empty list
    new_arr = []

    # loop array according to the operations
    for operations in list_operations:
        new_arr = arr.copy()
        # remove index from copy list of all list
        new_arr.pop(arr.index(arr[operations[1]]))
        new_arr.pop(arr.index(arr[operations[0]]))
        # insert values with operations and buffer values
        new_arr.insert(operations[0],arr[operations[1]])
        new_arr.insert(operations[1],arr[operations[0]])
        # rebuild buffer
        arr = new_arr

    print("final",new_arr)
    return (new_arr) 


if __name__ == '__main__':
    arr = [5,3,2,1,3]
    list_operations = [[0,1],[1,3]]

    performOperations(arr, list_operations)