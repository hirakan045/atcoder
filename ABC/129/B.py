def main() -> None:
    N = int(input())
    W = list(map(int, input().split()))

    ans = 10**6
    for i in range(N+1):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        ans = min(ans, abs(s1-s2))

    print(ans)

if __name__ == "__main__":
    main()