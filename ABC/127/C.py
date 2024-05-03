def main() -> None:
    N, M = map(int, input().split())

    L = 0
    R = N
    for _ in range(M):
        l, r = map(int, input().split())
        L = max(L, l)
        R = min(R, r)

    ans = R - L + 1
    if ans > 0:
        print(ans)
    else:
        print(0)

if __name__ == "__main__":
    main()