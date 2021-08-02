#P1.2
import math

g = -9.81

def time_in_air( h0, v0):
    return - (v0 + math.sqrt(v0**2 - 2* g *h0)) / g

def main():
    print('Computing the height in meters of an object',
    'with initial height h0 and velocity v0:')
   
    while True:
        s = input('Press q to quit or anything else to continue: ')
        
        if s == 'q':
            break
        
        h0 = input('Enter initial height: ')
        h0 = float(h0)
        v0 = input('Enter initial velocity: ')
        v0 = float(v0)
        
        tair = time_in_air(h0,v0)
        
        print('Time in air is = %.2f seconds.' % tair)

main()