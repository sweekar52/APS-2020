
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    x=arr[0]+arr[1]+arr[2]+arr[3]
    print(x,end=" ")
    x=arr[2]+arr[1]+arr[3]+arr[4]
    print(x)    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)