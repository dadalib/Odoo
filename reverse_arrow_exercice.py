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

def performOperations(arr, operations):
    """Calculate how many steps you need for your target 
    
    Parameters
    ----------
    arr : list
    operationn : list

    Returns:
    --------
    new_arr : list
    """

    # loop the list until it match the target
    while tools[startIndex] != target:
        # incriment the index and steps counter 
        if tools[startIndex] != target:
            startIndex += 1
            steps += 1

        
    print ("steps",steps)
    # return steps
    return steps  

if __name__ == '__main__':
    tools = [5,3,2,1,3]
    startIndex = [[0,1],[1,3]]