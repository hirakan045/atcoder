n = int(input())

for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-j-i):
            print(i, j, k)