# AP-Multithreading-Assignment
This repository contains three Python programs that demonstrate the use of Python's `threading` module for improving performance through parallel execution. The programs compare single-threaded and multi-threaded approaches for merge sort, quicksort, and file downloading tasks.

## Q1. Threaded Merge Sort
The program uses implements both a single threaded version and a multi-threaded version of the merge sort algorithm, and compares the running time of both versions. It uses python's `threading` module to split the list into two halves and sorts each list using in-place .sort() and merges them. 

## Q2. Threaded Quick Sort
The code implements both a single-threaded and a multi-threaded version of the quicksort algorithm to sort a list of random integers. The multi-threaded version uses python's `threading` module to recursively sort subarrays in parallel, with a thread limit controlled by a global counter and lock to prevent excessive thread creation. It then compares the execution time of both methods and ensures that the sorted outputs are identical.

## Q3. Concurrent File Downloader
This Python program downloads multiple files sequentially and concurrently using threads and compares the time taken by both approaches. It accepts file URLs one afer another directly from user input or all the urls from a text file. Each file is downloaded using the `requests` module, and concurrent downloads are handled using Python’s `threading` module by creating a thread for each file. The total time taken for both concurrent and sequential downloads is calculated.

# Requirements
- Python 3.x
- `requests` module: install using `pip install requests`
