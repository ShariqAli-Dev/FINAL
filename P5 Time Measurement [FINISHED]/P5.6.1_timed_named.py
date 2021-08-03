import time

def timed_name():
    start = time.time()
    name = input("What is your name? ")
    end = time.time()

    print(f"Hello {name}, it took you {end - start} time to answer.")

timed_name()