def main() -> None:
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    x = 0
    ans = 0
    for l in L:
        if x <= X:
            x += l
            ans += 1
        else:
            break

    if x <= X:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()