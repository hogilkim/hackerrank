#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def minimumBribes(q):
    # Write your code here
    
    q = [i-1 for i in q]
    bribe = 0
    for curr, og in enumerate(q):
        if og - curr >2:
            print("Too chaotic"); return;
        for val in q[max(og-1, 0):curr]:
            if val > og:
                bribe += 1
    
    print(bribe)

    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
