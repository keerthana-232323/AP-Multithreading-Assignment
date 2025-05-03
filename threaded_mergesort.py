import threading
import time
import random


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    midpoint = len(numbers) // 2
    left_half = merge_sort(numbers[:midpoint])
    right_half = merge_sort(numbers[midpoint:])
    return merge_lists(left_half, right_half)


def merge_lists(list_a, list_b):
    merged = []
    i = 0
    j = 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1

    merged.extend(list_a[i:])
    merged.extend(list_b[j:])
    return merged


def parallel_merge_sort(data):
    """Perform a simplified multi-threaded merge sort."""
    if len(data) <= 1:
        return data

    midpoint = len(data) // 2
    left_part = data[:midpoint]
    right_part = data[midpoint:]

    left_thread = threading.Thread(target=lambda: left_part.sort())
    right_thread = threading.Thread(target=lambda: right_part.sort())

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return merge_lists(left_part, right_part)


list_size = 100000
unsorted_list = [random.randint(0, 1000000) for _ in range(list_size)]

start = time.time()
sorted_by_single_thread = merge_sort(unsorted_list.copy())
single_thread_duration = time.time() - start
print(f"Single-threaded merge sort took: {single_thread_duration:.4f} seconds")

start = time.time()
sorted_by_multi_thread = parallel_merge_sort(unsorted_list.copy())
multi_thread_duration = time.time() - start
print(f"Multi-threaded merge sort took: {multi_thread_duration:.4f} seconds")

assert sorted_by_single_thread == sorted_by_multi_thread, "Mismatch in sorting results!"
