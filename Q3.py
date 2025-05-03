import os
import threading
import time
import requests
from urllib.parse import urlparse


def download_single_file(link):
    try:
        file_name = os.path.basename(urlparse(link).path)
        if not file_name:
            file_name = "downloaded_file"

        with requests.get(link, stream=True) as response:
            response.raise_for_status()
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        print(f"Downloaded: {file_name}")
    except Exception as error:
        print(f"Failed to download {link}: {error}")


def download_sequentially(links):
    for link in links:
        download_single_file(link)


def download_concurrently(links):
    threads = []
    for link in links:
        thread = threading.Thread(target=download_single_file, args=(link,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def fetch_urls():
    print("Paste URLs one per line. To stop, press Enter on an empty line.")
    print("Alternatively, enter a file path containing URLs:")

    initial_input = input().strip()
    url_list = []

    if os.path.isfile(initial_input):
        try:
            with open(initial_input, "r") as file:
                url_list = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Couldn't read file {initial_input}: {e}")
    elif initial_input:
        url_list.append(initial_input)
        while True:
            next_line = input().strip()
            if not next_line:
                break
            url_list.append(next_line)

    return url_list


def main():
    urls_to_download = fetch_urls()
    if not urls_to_download:
        print("No URLs provided. Exiting...")
        return

    print(f"\nStarting concurrent download of {len(urls_to_download)} files...")
    start_time = time.time()
    download_concurrently(urls_to_download)
    concurrent_duration = time.time() - start_time

    print(f"\nStarting sequential download of {len(urls_to_download)} files...")
    start_time = time.time()
    download_sequentially(urls_to_download)
    sequential_duration = time.time() - start_time

    print("\nSummary of download times:")
    print(f"Concurrent: {concurrent_duration:.2f} seconds")
    print(f"Sequential: {sequential_duration:.2f} seconds")


if __name__ == "__main__":
    main()
