### Conclusions

As a result of tests on sorting lists of different sizes (10, 100, 1000, 10000 elements) using different sorting algorithms, the following results were obtained:

- Timsort is the fastest algorithm for all array sizes. It significantly outperforms both Insertion Sort and Merge Sort on all tested datasets.
- Merge Sort shows stable results and performs better than Insertion Sort, especially on larger arrays.
- Insertion Sort shows the worst performance, especially on large arrays, where the execution time is much longer compared to other algorithms.



Bottom line:
Timsort, as a built-in sorting method in Python, is the most efficient choice in most cases due to its optimization and hybrid approach that combines merge and insertion sorting. Programmers most often use Python's built-in sorting algorithms because they are already optimized for a wide range of tasks.
