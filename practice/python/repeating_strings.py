#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    # c contains all of the original a's
    c = s.count("a")

    number_of_repeats = n // len(s)

    if n % len(s) == 0:
        c = c * number_of_repeats

    else:
        m = n % len(s)
        c = c * number_of_repeats + s[:m].count("a")

    return c


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + "\n")

    fptr.close()
