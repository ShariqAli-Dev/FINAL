a = float(input("Type a real number a: "))
b = float(input("Type a real number b: ")) 
x = -b / a

if a == "0":
  print("No solution")
elif b == "0":
  print("All solutions")
else:
  print(f'x = {x}')