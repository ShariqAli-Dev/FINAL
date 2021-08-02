#P1.1
# velocity of object after t seconds
#  - v(t) = gt + VInit

g = -9.81

def velocity(t, v0):
    return g*t + v0

def main():
    print("Computing the velocity in meters per second of an object with time t and initial velocity v0: ")

    while True:
        s = input("Press q to quit or anything else to continue: ")

        if s.lower() == "q":
            break
        
        t = float(input("Enter Time: "))
        v0 = float(input("Enter Initial Velocity: "))
        final_velocity = velocity(t, v0)

        print(final_velocity)

main()