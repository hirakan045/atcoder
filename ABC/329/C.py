from collections import defaultdict

def main() -> None:
    N = int(input())
    S = input()
    D = defaultdict(int)

    count = 1
    for i in range(N-1):
        target = S[i]
        next = S[i+1]
        if target == next:
            count += 1
        else:
            count = 1
        if D[target] < count:
            D[target] = count

    ans = 0
    for k, v in D.items():
        ans += v

    if N == 1:
        print(1)
    else:
        print(ans)

if __name__ == "__main__":
    main()