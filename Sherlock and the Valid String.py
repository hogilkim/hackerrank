#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter
def isValid(s):
    # Write your code here
    YES, NO = "YES", "NO"
    counter = Counter(s)
    
    freqs_counter = Counter(counter.values())

    if len(freqs_counter) > 2: return NO
    if len(freqs_counter) == 1: return YES
    # key1 < key2
    key1, key2 = sorted(freqs_counter.keys())
    
    if key2-key1 == 1 and freqs_counter[key2] == 1:
        return YES
    if freqs_counter[key1] == 1: return YES
    return NO
    
    return ""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
