import math

d = int(input())
square_d = math.floor(d**(1/2))+1

results = []
for i in range(square_d):
    if i**2 < d:
        miny = math.floor((d - i ** 2) ** (1 / 2))
        maxy = math.floor((d - i ** 2) ** (1 / 2)) + 1
        results.append(abs(i ** 2 + miny ** 2 - d))
        results.append(abs(i ** 2 + maxy ** 2 - d))
    else:
        y = 0
        results.append(i**2 - d)

print(min(results))