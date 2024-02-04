H, W, N = map(int, input().split())

area = [["." for w in range(W)] for h in range(H)]

x, y, z = 0, 0, 0

for i in range(N):
    if area[y][x] == ".":
        area[y][x] = "#"
        z += 1
    else:
        area[y][x] = "."
        z -= 1
    if z % 4 == 0:
        y = (y - 1) % H
    elif z % 4 == 1:
        x = (x + 1) % W
    elif z % 4 == 2:
        y = (y + 1) % H
    else:  # z % 4 == 3
        x = (x - 1) % W

for i in range(H):
    print("".join(area[i]))
