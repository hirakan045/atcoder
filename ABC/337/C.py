n = int(input())

a = list(map(int, input().split()))
distance_cache = {}
result = [0] * n

for i in range(n):
    distance = 0
    current = i
    path = []
    # i番目の人の距離を調べる
    next_person = a[current]
    # 先頭の場合
    if next_person == -1:
        distance_cache[i] = 0
        result[0] = i + 1
    while next_person != -1:
        # 距離が計算されている場合
        if current in distance_cache:
            distance += distance_cache[current]
            break
        else:
            # 経路を追加
            path.append(current)
            # 次の人を調べる
            current = next_person - 1
            next_person = a[current]
            distance += 1
    # 調べた距離を保存する
    for p in path:
        distance_cache[p] = distance
        distance -= 1
    result[distance_cache[i]] = i + 1

print(*result)