#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    ans = ""
    k = k % 26
    n = len(s)
    for i in range(n):
        if not s[i].isalpha():
            ans += s[i]
        else:
            if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
                tmp = ((ord(s[i]) - ord('a')) + k) % 26
                ans += chr(ord('a') + tmp)
            if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
                tmp = ((ord(s[i]) - ord('A')) + k) % 26
                ans += chr(ord('A') + tmp)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()