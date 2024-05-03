def main() -> None:
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = []
    for a in A:
        if a % K == 0:
            ans.append(str(a // K))

    print(" ".join(ans))


if __name__ == "__main__":
    main()