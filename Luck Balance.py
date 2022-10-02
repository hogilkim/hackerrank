#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
import heapq
def luckBalance(k, contests):
    # Write your code here
    total_luck = 0
    
    max_heap = []
    heapq.heapify(max_heap)
    
    for luck, important in contests:
        if not important:
            total_luck += luck
        
        else:
            heapq.heappush(max_heap, -luck)
    
    while k and max_heap:
        total_luck -= heapq.heappop(max_heap)
        k -= 1
    
    return total_luck + sum(max_heap)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
