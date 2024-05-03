def main() -> None:
    from collections import defaultdict

    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    d = defaultdict(bool)

    ans = K * (1+K) // 2

    for a in A:
        if d[a] or a > K:
            continue
        else:
            ans -= a
            d[a] = True

    print(ans)

if __name__ == "__main__":
    main()