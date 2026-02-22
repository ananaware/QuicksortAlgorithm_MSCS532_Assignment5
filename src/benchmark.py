import time
import random
import csv
import statistics
import sys

from quicksort_deterministic import quicksort as deterministic_quicksort
from quicksort_randomized import randomized_quicksort

sys.setrecursionlimit(20000)

def benchmark_version(func, arr, trials=10):
    times = []
    for _ in range(trials):
        arr_copy = arr.copy()
        start = time.perf_counter()
        func(arr_copy, 0, len(arr_copy) - 1)
        end = time.perf_counter()
        times.append(end - start)
    return statistics.mean(times), statistics.stdev(times)

input_sizes = [1000, 5000, 10000]

distributions = {
    "random": lambda n: [random.randint(0, n) for _ in range(n)],
    "sorted": lambda n: list(range(n)),
    "reverse": lambda n: list(range(n, 0, -1))
}

with open("results/quicksort_bench.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["version", "distribution", "n", "avg_time", "std_dev"])

    for n in input_sizes:
        for name, gen in distributions.items():
            base = gen(n)

            avg_det, std_det = benchmark_version(deterministic_quicksort, base)
            writer.writerow(["deterministic", name, n, avg_det, std_det])

            avg_rand, std_rand = benchmark_version(randomized_quicksort, base)
            writer.writerow(["randomized", name, n, avg_rand, std_rand])

print("Benchmark completed. Results saved to results/quicksort_bench.csv")