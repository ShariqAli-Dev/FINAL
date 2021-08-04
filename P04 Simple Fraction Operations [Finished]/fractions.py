def gcd(a,b):
  r0 = a
  r1 = b
  while r1 != 0:
    r2 = r0 % r1
    r0 = r1
    r1 = r2
  return r0
def main():
  while True: # Continue until 'q' is entered
    ans = input('Press q to quit or a pair of integers: ')
    if ans == 'q':
      break
    ans = ans.split(' ') # Separate the input in two integers
    a = int(ans[0])
    b = int(ans[1])
    g = gcd(a,b) # Call the gcd function
    print('gcd({},{}) = {}'.format(a,b,g))
main()

def num(f):
  f = f.split('/')
  return int(f[0])
def den(f):
  f = f.split('/')
  if len(f) == 1:
    return 1
  else:
    return int(f[1])
def reduce(f):
  n = num(f) # Call to the new function num
  d = den(f) # Call to the new function den
  # Regularization of the fraction (as before)
  g = gcd(n,d)
  n = n//g
  d = d//g
  if d < 0:
    n *= -1
    d *= -1
  if d == 1:
    return str(n)
  else:
    return str(n)+'/'+str(d)
def decimal(f):
  return num(f)/den(f)
def main():
  while True:
    ans = input('Press q to quit or a fraction to continue: ')
    if ans == 'q':
      break
    f = reduce(ans)
    fd = decimal(f)
    print('{} = {} = {}'.format(ans,f,fd))
main()

def add(f1,f2):
  n1 = num(f1)
  d1 = den(f1)
  n2 = num(f2)
  d2 = den(f2)
  n = n1*d2+d1*n2 # Numerator of the sum
  d = d1*d2 # Denominator of the sum
  f = reduce(str(n) + '/' + str(d)) # Reduce the result
  return f
def division(f1, f2):
  n1 = num(f1)
  d1 = den(f1)
  n2 = num(f2)
  d2 = den(f2)
  n = n1*d2
  d = d1*n2
  f = reduce(str(n) + '/' + str(d)) # Reduce the result
  return f
def sub(f1, f2):
  n1 = num(f1)
  d1 = den(f1)
  n2 = num(f2)
  d2 = den(f2)
  n = n1*d2-d1*n2 # Numerator of the sum
  d = d1*d2 # Denominator of the sum
  f = reduce(str(n) + '/' + str(d)) # Reduce the result
  return f
  
  
  
  
def main():
  while True:
    ans = input('Press q to quit or a pair of fractions or integers to continue: ')
    if ans == 'q':
      break
    ans = ans.split(' ') # Separate the two operands from the input
    f = reduce(ans[0])
    g = reduce(ans[1])
    #Addition
    res = add(f,g)
    print('{} + {} = {}'.format(f,g,res))
    fd = decimal(f)
    gd = decimal(g)
    resd = decimal(res)
    print('{} + {} = {}'.format(fd,gd,resd))
    
    #Division 
    re = division(f,g)
    print('{} / {} = {}'.format(f,g,resd))
    fd = decimal(f)
    gd = decimal(g)
    resd = decimal(re)
    print('{} + {} = {}'.format(fd,gd,resd))


main()