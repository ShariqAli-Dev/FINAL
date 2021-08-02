import math

g = -9.81

def time_in_air( h0, v0):
    return - (v0 + math.sqrt(v0**2 - 2* g *h0)) / g

def main():
    print('Computing the height in meters of an object',
    'with initial height h0 and velocity v0:\n')
   
    while True:
        s = input('Press q to quit or anything else to continue:\n')
        
        if s == 'q':
            break
        
        h0 = float(input('Enter initial height: '))
        v0 = float(input('Enter initial velocity: '))   
        tair = time_in_air(h0,v0)
        
        print(f'\nTime in air is {tair} seconds.')

main()