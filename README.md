# Quicksort Algorithm: Implementation, Analysis, and Randomization  
MSCS 532 – Algorithms and Data Structures  
University of the Cumberlands  

---

## Overview

This project implements both deterministic and randomized versions of the Quicksort algorithm in Python. It includes:

- Theoretical time and space complexity analysis
- Empirical performance comparison
- Statistical evaluation (average and standard deviation)
- Analysis of the impact of randomization

The implementation is based on concepts from:

> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

---

## Project Structure


MSCS532_Assignment5_Quicksort/
│
├── src/
│ ├── quicksort_deterministic.py
│ ├── quicksort_randomized.py
│ └── benchmark.py
│
├── results/
│ └── results.csv
│
├── report/
│ └── Assignment_Report.pdf
│
├── tests/
│ └── test_quicksort.py
│
└── README.md


---

##  Implementation Details

### Deterministic Quicksort
- Uses Lomuto partition scheme
- Pivot = last element
- Worst-case behavior on sorted/reverse-sorted inputs

- Deterministic pivot strategy: always selects the last element

### Randomized Quicksort
- Random pivot selection
- Reduces probability of worst-case O(n²)
- Maintains expected O(n log n)

---

## Empirical Analysis

Each experiment was executed:

- 10 independent trials
- For input sizes: 1000, 2000, 5000, 10000
- For input types:
  - Random
  - Sorted
  - Reverse Sorted

For each configuration, we computed:

- Average running time
- Standard deviation

Results are saved in:
```bash


results/results.csv
```

---

## Sample Output

Example benchmark execution:


Completed n=1000, case=random
Completed n=1000, case=sorted
Completed n=1000, case=reverse
...
Results saved to results/results.csv


Example CSV output:


Size,Case,Algorithm,Average Time (s),Std Dev (s)
1000,random,Deterministic,0.00121,0.00008
1000,random,Randomized,0.00118,0.00005


---

##  Key Observations

1. Deterministic Quicksort performs efficiently on random inputs.
2. Deterministic Quicksort degrades significantly on sorted inputs.
3. Deep recursion was observed for sorted input, reflecting worst-case O(n²).
4. Randomized Quicksort maintained stable performance across all input types.
5. Standard deviation values confirmed lower performance variability for randomized Quicksort.

---

## Theoretical Alignment

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)
- Space Complexity (average): O(log n)
- Space Complexity (worst): O(n)

Empirical results strongly align with theoretical analysis from CLRS (2022).

---

### Why O(n log n) vs O(n²)?

Quicksort achieves O(n log n) time when partitions are balanced, meaning each recursive call splits the array into roughly two equal halves. This results in log n recursion depth with O(n) work per level.

In the worst case, when the pivot always produces highly unbalanced partitions (e.g., sorted input with last-element pivot), the recursion depth becomes n, leading to O(n²) total comparisons. This behavior was empirically observed during benchmarking.
---

## How to Run

From project root:

### Run Edge Case Tests
```bash

python edge_case_check.py
```

### Run Benchmark
```bash

python src/benchmark.py
```

Results will be saved to:
```bash
results/results.csv

```
---

## What I Learned

Through this assignment, I learned:

- How pivot selection directly impacts recursion depth
- Why worst-case O(n²) is not just theoretical but observable
- How randomization improves algorithmic stability
- The importance of running multiple trials and computing statistical measures
- How empirical data supports theoretical complexity analysis

---

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms*