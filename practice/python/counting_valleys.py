#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == "U":
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == "U" and seaLevel == 0:
            valley += 1

    return valley


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + "\n")

    fptr.close()
