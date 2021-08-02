from math import sqrt

a = float(input("Type a real number a: "))
b = float(input("Type a real number b: "))
c = float(input("Type a real number c: "))
d = (b**2) - (4 * a * c)

if 4 * a * c > b**2:
  print("No real solution")

sol1 = (-b - sqrt(d)) / (2 * a)
sol2 = (-b + sqrt(d)) / (2 * a)

print(f'The solution are {sol1} and {sol2}')
