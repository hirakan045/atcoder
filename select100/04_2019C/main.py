n, m = map(int, input().split())

points = []
for i in range(n):
    points.append([int(i) for i in input().split()])

results = []
for t1 in range(m-1):
    for t2 in range(t1, m):
        point = 0
        for i in range(n):
            point += max([points[i][t1], points[i][t2]])
        results.append(point)

print(max(results))