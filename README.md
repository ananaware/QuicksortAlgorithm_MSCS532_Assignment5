\# MSCS 532 – Assignment 5  

\## Quicksort Implementation, Analysis, and Randomization  



This repository contains the implementation and analysis of deterministic and randomized Quicksort algorithms as part of MSCS 532 – Algorithms and Data Structures.



---



\## Repository Structure

```bash

src/

quicksort\_deterministic.py

quicksort\_randomized.py

benchmark.py



report/

MSCS532\_Assignment5\_Quicksort\_Report.pdf



results/

Screenshots of outputs and benchmark results

```



---



\## Implementations



\### Deterministic Quicksort

\- Uses Lomuto partition scheme

\- Last element selected as pivot

\- Based on CLRS Chapter 7



\### Randomized Quicksort

\- Random pivot selection

\- Reduces likelihood of worst-case behavior

\- Expected time complexity: O(n log n)



---



\## How to Run



From the project root directory:



Run deterministic version:

```bash

python src/quicksort\_deterministic.py

```



Run randomized version:

```bash

python src/quicksort\_randomized.py

```



Run empirical benchmark:

```bash

python src/benchmark.py

```



---



\## Key Findings



\- Deterministic Quicksort performs efficiently on random input.

\- It degrades to O(n²) on sorted and reverse-sorted input.

\- Randomized Quicksort maintains expected O(n log n) performance across all tested input types.

\- Experimental results strongly align with theoretical analysis from CLRS (2022).



---



\## Reference



Cormen, T. H., Leiserson, C. E., Rivest, R. L., \& Stein, C. (2022). \*Introduction to Algorithms\* (4th ed.). MIT Press.









