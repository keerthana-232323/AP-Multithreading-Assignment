# AP-Multithreading-Assignment
This repository contains three Python programs that demonstrate the use of Python's `threading` module for improving performance through parallel execution. The programs compare single-threaded and multi-threaded approaches for merge sort, quicksort, and file downloading tasks.

## Q1. Threaded Merge Sort
This program implements both a single-threaded and a multi-threaded version of the Merge Sort algorithm. The multi-threaded version uses Python's `threading` module to divide the list into two halves, sorts them using built-in methods for simplicity, and merges them back together. Execution times for both versions are compared.

## Q2. Threaded Quick Sort
The code implements both a single-threaded and a multi-threaded version of the quicksort algorithm to sort a list of random integers. The multi-threaded version uses python's `threading` module to recursively sort subarrays in parallel, with a thread limit controlled by a global counter and lock to prevent excessive thread creation. It then compares the execution time of both methods and ensures that the sorted outputs are identical.

## Q3. Concurrent File Downloader
This Python program downloads multiple files sequentially and concurrently using threads and compares the time taken by both approaches. It accepts file URLs one after another directly from user input or all the urls from a text file. Each file is downloaded using the `requests` module, and concurrent downloads are handled using Python’s `threading` module by creating a thread for each file. The total time taken for both concurrent and sequential downloads is calculated.

# Requirements
- Python 3.x
- `requests` module: install using `pip install requests`

# How to Run
``` bash
python Q1.py
python Q2.py
python Q3.py
```
# Sample Output
## Q1. Threaded Merge Sort
```bash
Single-threaded merge sort took: 0.3087 seconds
Multi-threaded merge sort took: 0.0442 seconds
```

## Q2. Threaded Quick Sort
```bash
Single-threaded quicksort took: 0.1900 seconds
Multi-threaded quicksort took: 0.1910 seconds
```
##  Q3. Concurrent File Downloader
```bash
Paste URLs one per line. To stop, press Enter on an empty line.
Alternatively, enter a file path containing URLs:
urls.txt

Starting concurrent download of 7 files...
Downloaded: dummy.pdf
Downloaded: sample-zip-file.zipDownloaded: sample-text-file.txt

Downloaded: Sample-jpg-image-50kb.jpg
Downloaded: PNG_transparency_demonstration_1.png
Downloaded: iso_8859-1.txt
Downloaded: addresses.csv

Starting sequential download of 7 files...
Downloaded: iso_8859-1.txt
Downloaded: addresses.csv
Downloaded: PNG_transparency_demonstration_1.png
Downloaded: dummy.pdf
Downloaded: sample-zip-file.zip
Downloaded: sample-text-file.txt
Downloaded: Sample-jpg-image-50kb.jpg

Summary of download times:
Concurrent: 2.04 seconds
Sequential: 4.20 seconds
```
