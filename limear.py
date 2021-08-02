import math

a = float(input("Type a real number a: ")) # float: real numbers
b = float(input("Type a real number b: ")) 
x=(-b/a)
if a=="0":
  print("No solution")
elif b=="0":
  print("All solutions")
else:
  print(f'x = {x}')

a = float(input("Type a real number a: ")) # float: real numbers
b = float(input("Type a real number b: ")) # float: real numbers
c = float(input("Type a real number c: "))
d = (b**2) - (4*a*c)
if 4*a*c>b**2:
  print("No real solution")

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
