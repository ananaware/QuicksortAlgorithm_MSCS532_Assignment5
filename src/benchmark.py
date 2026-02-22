import random
import time
import csv
import statistics

from quicksort_deterministic import quicksort
from quicksort_randomized import randomized_quicksort


def generate_array(n, case_type="random"):
    if case_type == "random":
        return [random.randint(0, 100000) for _ in range(n)]
    elif case_type == "sorted":
        return list(range(n))
    elif case_type == "reverse":
        return list(range(n, 0, -1))
    else:
        raise ValueError("Unknown case type")


def measure_time(sort_function, arr):
    start = time.perf_counter()
    sort_function(arr)
    end = time.perf_counter()
    return end - start


def run_experiment():
    sizes = [1000, 2000, 5000, 10000]
    cases = ["random", "sorted", "reverse"]
    trials = 10

    with open("results/results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Size",
            "Case",
            "Algorithm",
            "Average Time (s)",
            "Std Dev (s)"
        ])

        for n in sizes:
            for case in cases:

                det_times = []
                rand_times = []

                for _ in range(trials):
                    arr = generate_array(n, case)

                    arr1 = arr.copy()
                    arr2 = arr.copy()

                    det_times.append(measure_time(quicksort, arr1))
                    rand_times.append(measure_time(randomized_quicksort, arr2))

                writer.writerow([
                    n,
                    case,
                    "Deterministic",
                    statistics.mean(det_times),
                    statistics.stdev(det_times)
                ])

                writer.writerow([
                    n,
                    case,
                    "Randomized",
                    statistics.mean(rand_times),
                    statistics.stdev(rand_times)
                ])

                print(f"Completed n={n}, case={case}")

    print("\nResults saved to results/results.csv")


if __name__ == "__main__":
    run_experiment()