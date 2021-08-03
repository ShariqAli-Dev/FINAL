import time

def count_to(n):
    for i in range(n):
        print(f"{i + 1}...")
        time.sleep(1)

count_to(10)