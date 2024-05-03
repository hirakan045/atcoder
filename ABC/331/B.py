N, S, M, L = map(int, input().split())

price_list = []
for s in range(20):
    for m in range(20):
        for l in range (10):
            if 6*s + 8*m + 12*l >= N:
                price_list.append(S*s + M*m + L*l)

print(min(price_list))