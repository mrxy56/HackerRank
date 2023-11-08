#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            zero += 1
    cnt = pos + neg + zero
    pos = pos / cnt
    neg = neg / cnt
    zero = zero / cnt
    
    print("%.6f"%pos)
    print("%.6f"%neg)
    print("%.6f"%zero)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)