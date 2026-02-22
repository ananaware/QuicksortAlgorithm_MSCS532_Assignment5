"""
Deterministic Quicksort Implementation
MSCS 532 - Assignment 5
Based on CLRS (4th Edition), Chapter 7
"""
import sys
sys.setrecursionlimit(20000)

from typing import List

def partition(arr, low, high):
    """
    Lomuto partition scheme.
    Selects the last element as pivot.
    Rearranges array so that elements <= pivot are left,
    elements > pivot are right.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low=0, high=None):
    """
    In-place deterministic quicksort.
    Automatically handles empty arrays.
    """

    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print("Original Array:", sample)

    quicksort(sample, 0, len(sample) - 1)

    print("Sorted Array:", sample)