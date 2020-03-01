#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    z=0
    n=ar_count
    i=0
    while i<=n:
        z=z+ar[i]
        i+=1
        if i==n:
            return z
            break
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
