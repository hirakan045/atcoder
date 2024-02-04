N = int(input())
A = [int(a) for a in input().split()]

result = 0
m = A[0]

for i in range(N):
    result += A[i]
    if m > result:
        m = result

if m < 0:
    print(result - m)
else:
    print(result)