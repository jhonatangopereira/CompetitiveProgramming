#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cardinalitySort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def cardinalitySort(nums):
    nums.sort(key=lambda num: (bin(num).count("1"), num))
    return nums
 
# Driver Code
arr = [ 31, 15, 7, 3, 2 ]
n = len(arr)
 
print(cardinalitySort(arr))
 

# def cardinalitySort(nums):
#   for i in nums:
#     print('{0:b}'.format(i).count('1'))
#   print(nums)


# a = [1, 2, 3, 4]
# cardinalitySort(a)
