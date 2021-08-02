#P1.4
g = -9.81

def top_height(h0, v0):
    return h0 - (v0**2) / (2 * g)

def main():
    print("Computing the hright in meters of an object with initial height h- and velocity v0: ")

    while True:
        s = input("Press q to quir or anything else to continue: ")
        
        if s.lower() == "q":
            break
        
        h0 = input('Enter initial height: ')
        h0 = float(h0)
        v0 = input('Enter initial velocity: ')
        v0 = float(v0)
        toph = top_height(h0,v0)
        print('top height = %.2f meters.' % toph)

main()