import time

def count_to_with_erasing(n):
    for i in range(n):
        print(f"{i + 1}...", end="\r")
        time.sleep(1)

count_to_with_erasing(10)