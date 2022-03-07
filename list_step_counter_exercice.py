#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER startIndex
#  3. STRING target
#

def toolchanger(tools, startIndex, target):
    """Calculate how many steps you need for your target 
    
    Parameters
    ----------
    tools : list
    startIndex : int
    target : str

    Returns:
    --------
    steps : int
    """
    # write your code here
    # check input list
    check_list = isinstance(tools,list)
    # check integer
    check_integer = isinstance(startIndex,int)
    # check target
    check_target = isinstance(target,str)
    # steps counter
    steps = 0

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
    tools = ["Kristina","Irina","Celine","Rebecca","Lea"]
    startIndex = 1
    target = "Rebecca"
    toolchanger(tools,startIndex,target)
