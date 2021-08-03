import time

def timer():
    print("Press enter to start \n")
    print("Enter 'Stop' to stop; pressing enter to record a lap")
    user_input = input("")
    total_time = 0
    total_laps = 0

    while True:
        start = time.time()
        user_input = input("")
        end = time.time()
        
        if user_input.lower() == 'stop':
            break
        
        total_laps += 1
        total_time += start + end
        
        print(f"Lap {total_laps}: {end - start} seconds\n")
    
    print(f"\nTotal: {total_time}")

timer()