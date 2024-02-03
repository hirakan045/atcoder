n = int(input())
a = list(map(int, input().split()))

next_person = {i: a[i] - 1 for i in range(n) if a[i] != -1}
result = [0] * n
distance_cache = {}

for i in range(n):
    distance = 0
    current = i
    path = []  # 現在のパスを追跡

    while current in next_person:
        if current in distance_cache:
            distance += distance_cache[current]
            break
        path.append(current)
        current = next_person[current]
        distance += 1

    for p in path:
        distance_cache[p] = distance
        distance -= 1

    # 先頭に立つ人は距離0
    distance_cache[i] = distance_cache.get(i, 0)
    result[distance_cache[i]] = i + 1

print(*result)
