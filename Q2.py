import threading
import time
import random

MAX_THREADS = 4
current_threads = 0
lock = threading.Lock()


def quicksort(arr, low, high):
    """Single-threaded quicksort implementation."""
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """Partition the array around a pivot."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def threaded_quicksort(arr, low, high):
    """Multi-threaded quicksort implementation."""
    global current_threads

    if low < high:
        pivot_index = partition(arr, low, high)

        with lock:
            can_spawn = current_threads < MAX_THREADS
            if can_spawn:
                current_threads += 1

        if can_spawn:
            left_thread = threading.Thread(target=threaded_quicksort, args=(arr, low, pivot_index - 1))
            right_thread = threading.Thread(target=threaded_quicksort, args=(arr, pivot_index + 1, high))
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()
            with lock:
                current_threads -= 1
        else:
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)


array_size = 100000
random_array = [random.randint(0, 1000000) for _ in range(array_size)]

single_threaded_array = random_array.copy()
start_time = time.time()
quicksort(single_threaded_array, 0, len(single_threaded_array) - 1)
single_thread_time = time.time() - start_time
print(f"Single-threaded quicksort took: {single_thread_time:.4f} seconds")

multi_threaded_array = random_array.copy()
start_time = time.time()
threaded_quicksort(multi_threaded_array, 0, len(multi_threaded_array) - 1)
multi_thread_time = time.time() - start_time
print(f"Multi-threaded quicksort took: {multi_thread_time:.4f} seconds")

assert single_threaded_array == multi_threaded_array, "The sorted arrays do not match!"
