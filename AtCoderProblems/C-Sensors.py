h, w = map(int, input().split())

area = []
for i in range(h):
    s = list(input())
    area.append(s)

for i in range(h):
    for j in range(w):
        print(area[i][j])
