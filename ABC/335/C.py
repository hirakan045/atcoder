import sys

n, q = map(int, input().split())
XY = [(i, 0) for i in range(1, n+1)][::-1]
for i in range(q):
    q1, q2 = sys.stdin.readline().rstrip().split()
    if q1 == "1":
        x, y = XY[-1]
        if q2 == "U": XY.append((x, y+1))
        elif q2 == "R": XY.append((x+1, y))
        elif q2 == "D": XY.append((x, y-1))
        else: XY.append((x-1, y))
    else:
        print(*XY[-int(q2)])