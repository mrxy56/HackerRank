#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


# Pay attention to the conversion between int and string, especially the previous 0s.
def timeConversion(s):
    # Write your code here
    time_format = s[8:10]
    ls = s[0:8].split(':')
    hh = int(ls[0])
    if time_format == 'PM':
        hh += 12
        if hh == 24:
            hh = 12
    if time_format == 'AM':
        if hh == 12:
            hh = 0
    hh = str(hh)
    if len(hh) == 1:
        hh = '0' + hh
    ls[0] = hh
    ans = ":".join(ls)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
