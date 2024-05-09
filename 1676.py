import math

N = int(input())

fac = str(math.factorial(N))

z = 0

for s in reversed(list(fac)):
    if s != '0':
        break
    
    z += 1

print(z)