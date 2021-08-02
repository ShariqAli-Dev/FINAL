g = -9.81

def top_height(h0, v0):
    return h0 - (v0**2) / (2 * g)

def main():
    print("Computing the hright in meters of an object with initial height h- and velocity v0:\n")

    while True:
        s = input("Press q to quir or anything else to continue:\n")
        
        if s.lower() == "q":
            break
        
        h0 = float(input('Enter initial height: '))
        v0 = float(input('Enter initial velocity: '))
        toph = top_height(h0,v0)
        
        print(f'\nTop Height = {toph} meters.')

main()