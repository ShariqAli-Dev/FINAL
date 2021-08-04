g = -9.81

def height(t, v0, h0):
    return (g/2 * t**2) + (v0 * t) + h0

def main():
    print("Computing height in meters of an object with time t, initial velocity v0, and initial height h0:\n")

    while True:
        s = input("Press q to quit or anything else to continue:\n")

        if s.lower() == "q":
            break

        t = float("Enter time: ")
        v0 = float("Enter initial velocity: ")
        h0 = float("Enter initial height: ")
        object_height_via_time = height(t, v0, h0)

        print(f"\nAfter {t} seconds, the object reaches a height of {object_height_via_time} meters")

main()