import sys
sys.setrecursionlimit(20000)

import random
import time
import copy
from quicksort_deterministic import quicksort as deterministic_quicksort
from quicksort_randomized import randomized_quicksort


def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(size))


def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))


def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    return end - start


def run_experiment():
    sizes = [1000, 5000, 10000]
    distributions = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array,
    }

    for size in sizes:
        print(f"\nArray Size: {size}")
        for name, generator in distributions.items():
            base_array = generator(size)

            arr1 = copy.deepcopy(base_array)
            arr2 = copy.deepcopy(base_array)

            det_time = measure_time(deterministic_quicksort, arr1)
            rand_time = measure_time(randomized_quicksort, arr2)

            print(f"{name} Input:")
            print(f"  Deterministic: {det_time:.6f} seconds")
            print(f"  Randomized   : {rand_time:.6f} seconds")


if __name__ == "__main__":
    run_experiment()