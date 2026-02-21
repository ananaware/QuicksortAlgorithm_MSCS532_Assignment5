"""
Randomized Quicksort Implementation
MSCS 532 - Assignment 5
Based on CLRS (4th Edition), Chapter 7
"""

import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr, low, high):
    """
    Randomly selects pivot and swaps with last element.
    """
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print("Original Array:", sample)

    randomized_quicksort(sample, 0, len(sample) - 1)

    print("Sorted Array:", sample)