#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    """. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number."""

    # Step 1 - Find the mode(s) of the array

    # arr = 1, 1, 2, 3, 3, 3, 3, 5
    total_counts = {}
    # Step - 1.1 - Find unique numbers
    unique_numbers = set(arr)

    #        1.2 - Count each unique number?
    # unique_numbers = 1, 2, 3, 5
    for num in unique_numbers:
        times_in_list = 0
        for internal_number in arr:
            if num == internal_number:
                times_in_list += 1
        total_counts[num] = times_in_list
    # {1: 2, 2: 1, 3:4, 5:1 }


    #  1.3 - identify largest count
    largest_count = max(total_counts.values()) 
    print("Largest - count: ", largest_count)

    numbers_with_largest_count = []
    # 1.4 - iddentify numbers w/ the largest coount
    for x in total_counts:
        # x is a key
        if total_counts[x] == largest_count:
            # X is one of my numbers
            numbers_with_largest_count.append(x)



    # Step 2 - Find the lowest number / sighting id out of the highest modes?
    lowest_number = min(numbers_with_largest_count)
    return lowest_number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

