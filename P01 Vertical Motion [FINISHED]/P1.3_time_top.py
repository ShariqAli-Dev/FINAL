g = -9.81

def time_top(v0):
    return -v0 / g

def main():
    print("Computing the time top after which the object reaches it's top height with initial velocity v0:\n ")

    while True:
        s = input("Press q to quir or anything else to continue: \n")

        if s.lower() == "q":
            break

        v0 = float(input("Enter initial velocity: "))
        t_top = time_top(v0)

        print(f"\nTime Top = {t_top} seconds")


