a, b, c, x, y = map(int, input().split())

price = 0
if x >= y:
    if a + b < 2*c:
        price = (a+b)*y
    else:
        price = c*2*y

    remain = x - y

    if a*remain > 2*c*remain:
        price += c*2*remain
    else:
        price += a*remain
else:
    if a + b < 2 * c:
        price = (a + b) * x
    else:
        price = c * 2 * x

    remain = y - x

    if b*remain > 2*c*remain:
        price += c * 2 * remain
    else:
        price += b * remain

print(price)