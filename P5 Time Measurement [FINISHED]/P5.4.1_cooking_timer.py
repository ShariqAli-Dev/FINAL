import time

def cooking_timer(hours, minutes, seconds):
    for h in range(hours, -1, -1):
        for m in range(minutes, -1, -1):
            for s in range(seconds):
                time.sleep(1)
                print(f"{h}:{m}:{60 - s}", end="\r")
            seconds = 60
        minutes = 59
    print("Finished")

cooking_timer(1, 1, 20)