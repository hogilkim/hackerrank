#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getPrefixScores(arr):
    # Write your code here
    MOD = 10**9+7
    sum1 = 0
    ssum = 0
    curmax = 0
    res = []
    
    
    for idx, num in enumerate(arr):
        sum1 += num
        ssum += sum1
        curmax = max(curmax, num)
        ans = (ssum + curmax*(idx+1))%MOD
        res.append(ans)
    return res
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPrefixScores(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
