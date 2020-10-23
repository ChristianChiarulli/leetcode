import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, socks):

    pairs = 0

    for sock_type in set(socks):
        pairs += socks.count(sock_type) // 2

    return pairs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
