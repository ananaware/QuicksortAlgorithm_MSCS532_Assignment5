import random
import copy

# Try both import styles depending on your repo structure
try:
    from src.quicksort_deterministic import quicksort as det_qs
    from src.quicksort_randomized import randomized_quicksort as rand_qs
    IMPORT_STYLE = "from src.*"
except Exception:
    from quicksort_deterministic import quicksort as det_qs
    from quicksort_randomized import randomized_quicksort as rand_qs
    IMPORT_STYLE = "local files (run inside src)"

def run_one_case(arr, name):
    expected = sorted(arr)

    a1 = copy.deepcopy(arr)
    a2 = copy.deepcopy(arr)

    det_qs(a1)
    rand_qs(a2)

    ok1 = (a1 == expected)
    ok2 = (a2 == expected)

    if not ok1 or not ok2:
        print("\nFAILED:", name)
        print("Input:     ", arr)
        print("Expected:  ", expected)
        print("Deterministic:", a1)
        print("Randomized:   ", a2)
        raise SystemExit(1)

def main():
    print("Import style:", IMPORT_STYLE)

    cases = [
        ([], "empty"),
        ([1], "single"),
        ([2, 1], "two elements"),
        ([1, 2, 3, 4, 5], "already sorted"),
        ([5, 4, 3, 2, 1], "reverse sorted"),
        ([3, 3, 3, 3], "all duplicates"),
        ([3, 1, 2, 3, 0, 2, 3], "mixed with duplicates"),
        ([-1, -3, 2, 0, -2], "negatives"),
    ]

    for arr, name in cases:
        run_one_case(arr, name)

    # Random stress tests
    random.seed(123)
    for n in [10, 50, 200]:
        for t in range(50):
            arr = [random.randint(-1000, 1000) for _ in range(n)]
            run_one_case(arr, f"random n={n} trial={t}")

    print("\nALL EDGE CASES PASSED ✅")

if __name__ == "__main__":
    main()