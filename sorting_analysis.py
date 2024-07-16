import timeit
import random
import matplotlib.pyplot as plt

# Реалізація сортування злиттям
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
    return arr

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функція для тестування алгоритмів
def test_sorting_algorithms():
    sizes = [100, 1000, 10000, 100000]
    merge_times = []
    insertion_times = []
    timsort_times = []

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        print(f"Array size: {size}")

        t1 = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        merge_times.append(t1)
        print(f"Merge Sort: {t1:.5f} seconds")

        t2 = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        insertion_times.append(t2)
        print(f"Insertion Sort: {t2:.5f} seconds")

        t3 = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        timsort_times.append(t3)
        print(f"Timsort (sorted): {t3:.5f} seconds")

        print()

    return sizes, merge_times, insertion_times, timsort_times

# Побудова графіків
def visualize_results(sizes, merge_times, insertion_times, timsort_times):
    plt.plot(sizes, merge_times, label="Merge Sort", marker='o')
    plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
    plt.plot(sizes, timsort_times, label="Timsort (sorted)", marker='o')
    plt.xlabel("Array size")
    plt.ylabel("Time (seconds)")
    plt.title("Performance of Sorting Algorithms")
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--")
    plt.show()

# Виконання тестування і побудова графіків
sizes, merge_times, insertion_times, timsort_times = test_sorting_algorithms()
visualize_results(sizes, merge_times, insertion_times, timsort_times)
