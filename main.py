import random
import timeit
import tabulate

# Implementation of insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Implementation of merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function for Timsort (using built-in sorted function)
def timsort(arr):
    return sorted(arr)

# Function to generate random data
def generate_random_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Function to measure execution time
def measure_time(func, data):
    start_time = timeit.default_timer()
    func(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Main function to run tests and print results
def main():
    sizes = [10, 100, 1000, 10000]
    results = []

    for size in sizes:
        data = generate_random_data(size)

        insertion_sort_data = data[:]
        merge_sort_data = data[:]
        timsort_data = data[:]

        insertion_sort_time = measure_time(insertion_sort, insertion_sort_data)
        merge_sort_time = measure_time(merge_sort, merge_sort_data)
        timsort_time = measure_time(timsort, timsort_data)

        results.append([size, insertion_sort_time, merge_sort_time, timsort_time])

    headers = ["Size", "Insertion Sort", "Merge Sort", "Timsort"]
    print(tabulate.tabulate(results, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()