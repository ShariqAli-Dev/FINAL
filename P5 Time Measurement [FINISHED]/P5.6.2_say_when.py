import time

def say_when():
    start = time.time()
    print("Tell me when to stop")
    print(" Now!")
    print(" Stop!")
    
    while True:
        userInput = input(" ")
        if userInput == "when":
            break
    end = time.time()
    print(f"\nIt took you {end - start} seconds")

say_when()